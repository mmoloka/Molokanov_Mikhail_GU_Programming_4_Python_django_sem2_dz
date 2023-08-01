from django.core.management.base import BaseCommand
from second_app.models import User, Order


class Command(BaseCommand):
    help = 'Get all orders by user id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            orders = Order.objects.filter(customer=user)
            for order in orders:
                products = order.prducts.all()
                text = list()
                for product in products:
                    text.append(str(product.pk))
                result = str(order) + '; product_ids: ' + '; '.join(text) + '\n'
                self.stdout.write(result)
