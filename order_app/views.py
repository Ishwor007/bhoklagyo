from uuid import uuid4
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import secrets 

from .models import Order, Cart, BillingLocation
from food_app.models import Food
from user_app.models import Customer

from user_app import views as user_views

@login_required
def orders(request):
    customer = Customer.objects.get(user_id=request.user.id)
    orders = Order.objects.filter(user=customer).exclude(order_status__in=(Order.CANCELLED, Order.DELIVERED))
    total = sum([Food.objects.get(id=order.item_id).unit_price*order.quantity for order in orders])
    return render(request, 'order_app/orders.html', {'orders': orders, 'total': total})

@login_required
def cart(request):
    customer = Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.filter(user=customer)
    
    return render(request, 'order_app/cart.html', {'items': cart})

@login_required
def add_to_cart(request, food_id):
    food = Food.objects.get(id=food_id)
    user = Customer.objects.get(user_id=request.user.id)
    cart,created = Cart.objects.get_or_create(user=user, item=food)
    if created:
        cart.save()
    return redirect('cart')

@login_required
def delete_from_cart(request, cart_id):
    cart = Cart.objects.get(item_id=cart_id)
    if cart:
        cart.delete()
    return redirect('cart')

@login_required
def order_all(request):
    customer = Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.filter(user_id=customer.id)
    orders = Order.objects.filter(user_id=customer.id, order_status=Order.PENDING)
    
    order_ids = [order.item_id for order in orders]
    request_id = uuid4().hex[:16].upper()
    for item in cart:
        if not item.item_id in order_ids:
            Order.objects.create(user=customer, item_id=item.item_id, quantity=1, request_id=request_id)

    return redirect('orders')

@login_required
def order_item(request, food_id):
    food = Food.objects.get(id=food_id)
    user = Customer.objects.get(user_id=request.user.id)
    exists = Order.objects.filter(user=user, item=food, order_status=Order.PENDING).exists()
    
    if exists:
        return redirect('orders')

    request_id = uuid4().hex[:16].upper()
    order = Order.objects.create(user=user, item=food, quantity=1, request_id=request_id)
    return render(request, 'order_app/checkout.html', {'orders': [order]})

@login_required
def delete_from_orders(request, order_id):
        order = Order.objects.get(id=order_id)
        print(order, order.order_status)
        if order and not order.order_status==order.ACCEPTED:
            order.order_status = order.CANCELLED
            order.save()
        return redirect('orders')

@login_required
def orders(request):
    customer = Customer.objects.get(user_id=request.user.id)
    orders = Order.objects.filter(user= customer).exclude(order_status__in=(Order.CANCELLED, Order.DELIVERED))
    return render(request, 'order_app/orders.html', {'orders': orders})

@login_required
def checkout(request):
    customer = Customer.objects.get(user_id=request.user.id)
    orders = Order.objects.filter(user_id=customer, order_status=Order.PENDING)
    total_orders = len(orders)

    total = sum([Food.objects.get(id=order.item_id).unit_price*order.quantity for order in orders])
    data =  {
        'orders': orders, 
        'total_orders': total_orders, 
        'total': total
    }
    
    return render(request, 'order_app/checkout.html',data)

@login_required
def billing_location_form(request):
    customer = Customer.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        address = request.POST.get('address')
        email = request.POST.get('email')
        
        orders = Order.objects.filter(user_id=customer, order_status=Order.PENDING)
        
        BillingLocation.objects.create(
                            request_id=orders[0].request_id,
                            first_name=first_name, 
                            last_name=last_name, 
                            address=address, 
                            email=email)
        for order in orders:
            order.order_status = Order.DELIVERED
            order.save()

        return redirect('/')
    else:
        return render(request, 'order_app/billing_address.html')


def verify_payment(request):
    # amount = request.GET.get('amount')
    # p_id = request.GET.get('p_id')
    # token = request.GET.get('token')
    # p_name = request.GET.get('p_name')
    # print(f"{amount=},{p_id=},{token=},{p_name=}")
    # if amount and p_id and token and p_name:

    id = request.GET.get('amount')
    
    if id:
        return JsonResponse({"success":True})
    return JsonResponse({'success':False})