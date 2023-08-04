import datetime

from django.shortcuts import render, get_object_or_404
from .models import User, Order, Product
from  datetime import date


def get_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user)
    order_products = dict()
    for order in orders:
        order_products[str(order)] = [str(product) for product in order.prducts.all()]
    context = {
        'title': 'Orders of customer',
        'user': user.name,
        'order_products': order_products,
    }
    return render(request, 'second_app/orders_of_user.html', context=context)


def get_products(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user)
    year_products = month_products = week_products = set()
    for order in orders:
        if date.today() - order.ordered_date <= datetime.timedelta(365):
            year_products.add(order.prducts.all())
        elif date.today() - order.ordered_date <= datetime.timedelta(30):
            month_products.add(order.prducts.all())
        elif date.today() - order.ordered_date <= datetime.timedelta(7):
            week_products.add(order.prducts.all())
    context = {
        'title': 'Products of customer',
        'user': user.name,
        'year_products': year_products,
        'month_products': month_products,
        'week_products': week_products,
    }
    return render(request, 'second_app/products_of_user.html', context=context)
