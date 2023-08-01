from random import randint

from django.core.management.base import BaseCommand
from second_app.models import User, Product, Order


class Command(BaseCommand):
    help = 'Create fake orders.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for _ in range(1, count + 1):
            customer = User.objects.get(id=randint(1, 10))
            total_price = 0.00
            products = set()
            for _ in range(randint(1, 5)):
                product = Product.objects.get(id=randint(1, 10))
                products.add(product)
                total_price += float(product.price)
            order = Order.objects.create(customer=customer, total_price=total_price)
            order.prducts.add(*products)
            order.save()
