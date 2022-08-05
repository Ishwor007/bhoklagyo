from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import permission_required

from .models import Order, Cart
from food_app.models import Food
from user_app.models import Customer

from user_app import views as user_views

def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_app/orders.html', {'orders': orders})

def cart(request):
    cart = Cart.objects.filter(user=request.user.id)
    return render(request, 'order_app/cart.html', {'items': cart})

def add_to_cart(request, food_id):
    if request.user.is_authenticated:
        food = Food.objects.get(id=food_id)
        user = Customer.objects.get(user_ptr_id=request.user.id)
        cart, created = Cart.objects.get_or_create(user=user, item=food)
        
        if created:
            cart.save()
        
        return redirect('cart')

    return redirect(user_views.login_page)

def delete_from_cart(request, food_id):
    if request.user.is_authenticated:

        cart = Cart.objects.get(id=food_id)
        if cart.user_id == request.user.id:
            cart.delete()
        #else show error message
        return redirect('cart')

    return redirect(user_views.login_page)

def order_all(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user.id)
        user = Customer.objects.get(user_ptr_id=request.user.id)
        for item in cart:
            user_orders = Order.objects.filter(user=user, item=item.item)
            if item not in user_orders:
                order = Order.objects.create(user=user, item=item.item, quantity=1)

        return redirect('orders')
    return redirect(user_views.login_page)

def order_item(request, food_id):
    if request.user.is_authenticated:
        food = Food.objects.get(id=food_id)
        user = Customer.objects.get(user_ptr_id=request.user.id)
        exists = Order.objects.filter(user=user, item=food)
        # orders.quantity = 1
        if exists:
            return redirect('orders')
        else:
            order = Order.objects.create(user=user, item=food, quantity=1)
            return redirect('orders')
    return redirect(user_views.login_page)

def delete_from_orders(request, food_id):
    if request.user.is_authenticated:

        order = Order.objects.get(id=food_id)
        if order.user_id == request.user.id:
            order.delete()
        #else show error message
        return redirect('orders')

    return redirect(user_views.login_page)

def orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=Customer.objects.get(user_ptr_id=request.user.id))
        return render(request, 'order_app/orders.html', {'orders': orders})
    return redirect(user_views.login_page)

def checkout(request):
    if request.user.is_authenticated:
        return render(request, 'order_app/checkout.html')
    return redirect(user_views.login_page)

def billing_location(request):
    if request.user.is_authenticated:
        full_name = request.POST['fullname']
        address = request.POST['address']
        email = request.POST['email']
        return render(request, 'order_app/checkout.html')
    return redirect(user_views.login_page)