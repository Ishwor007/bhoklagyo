from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import permission_required

from .models import Order, Cart, BillingLocation
from food_app.models import Food
from user_app.models import Customer

from user_app import views as user_views

def orders(request):
    orders = Order.objects.filter(user=Customer.objects.get(user_id=request.user.id))
    total = sum([Food.objects.get(id=order.item_id).unit_price*order.quantity for order in orders])
    return render(request, 'order_app/orders.html', {'orders': orders, 'total': total})

def cart(request):
    cart = Cart.objects.filter(user=Customer.objects.get(user_id=request.user.id))
    
    return render(request, 'order_app/cart.html', {'items': cart})

def add_to_cart(request, food_id):
    if request.user.is_authenticated:
        food = Food.objects.get(id=food_id)
        user = Customer.objects.get(user_id=request.user.id)
        cart,created = Cart.objects.get_or_create(user=user, item=food)
        if created:
            cart.save()
        return redirect('cart')

    return redirect(user_views.login_page)

def delete_from_cart(request, cart_id):
    if request.user.is_authenticated:

        cart = Cart.objects.get(item_id=cart_id)
        if cart:
            cart.delete()
        #else show error message
        return redirect('cart')
    return redirect(user_views.login_page)

def order_all(request):
    if request.user.is_authenticated:        
        customer = Customer.objects.get(user_id=request.user.id)
        cart = Cart.objects.filter(user_id=customer.id)
        user_orders = Order.objects.filter(user_id=customer.id)
        
        order_ids = [user_orders.item_id for user_orders in user_orders]
        
        for item in cart:
            if not item.item_id in order_ids:
                Order.objects.create(user=customer, item_id=item.item_id, quantity=1)

        return redirect('orders')
    return redirect(user_views.login_page)

def order_item(request, food_id):
    if request.user.is_authenticated:
        food = Food.objects.get(id=food_id)
        user = Customer.objects.get(user_id=request.user.id)
        exists = Order.objects.filter(user=user, item=food)
        if exists:
            return redirect('orders')
        else:
            Order.objects.create(user=user, item=food, quantity=1)
            return redirect('orders')
    return redirect(user_views.login_page)

def delete_from_orders(request, order_id):
    if request.user.is_authenticated:

        order = Order.objects.get(id=order_id)
        if order:
            order.delete()
        #else show error message
        return redirect('orders')

    return redirect(user_views.login_page)

def orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=Customer.objects.get(user_id=request.user.id))
        return render(request, 'order_app/orders.html', {'orders': orders})
    return redirect(user_views.login_page)

def checkout(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user_id=Customer.objects.get(user_id=request.user.id))
        total_orders = len(orders)
        total = sum([Food.objects.get(id=order.item_id).unit_price*order.quantity for order in orders])
        data =  {
            'orders': orders, 
            'total_orders': total_orders, 
            'total': total
        }
        
        return render(request, 'order_app/checkout.html',data)
    return redirect(user_views.login_page)

def billing_location_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            address = request.POST.get('address')
            email = request.POST.get('email')
            orders = Order.objects.filter(user_id=Customer.objects.get(user_id=request.user.id))

            quantity = [request.POST.get(f'quantity-{order.id}') for order in orders]
            
            for i,order in enumerate(orders):
                order.quantity = quantity[i]
                order.save()
                # BillingLocation.objects.create( order_id=order.id, 
                #                     first_name=first_name, 
                #                     last_name=last_name, 
                #                     address=address, 
                #                     email=email)
            total_orders = len(orders)
            total = sum([Food.objects.get(id=o.item_id).unit_price*float(q) for o,q in zip(orders,quantity)])
            data =  {
                'orders': orders, 
                'total_orders': total_orders, 
                'total': total
            }
            return render(request, 'order_app/checkout.html', data)
        else:
            return render(request, 'order_app/billing_address.html')
    return redirect(user_views.login_page)


