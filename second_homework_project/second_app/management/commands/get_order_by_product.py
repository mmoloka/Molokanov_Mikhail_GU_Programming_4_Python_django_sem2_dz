from django.core.management.base import BaseCommand
from second_app.models import User, Product, Order


class Command(BaseCommand):
    help = 'Get all orders by product'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            orders = Order.objects.all()
            for order in orders:
                products = order.prducts.all()
                if product in products:
                    result = str(order) + '; customer_id: ' + str(order.customer.pk)
                    self.stdout.write(result)
