from django.core.management.base import BaseCommand, CommandParser
from second_app.models import User, Product
from random import randint


class Command(BaseCommand):
    help = 'Create fake users and products.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='User and Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'example{i}@mail.com', phone=89991234567 + i,
                        address=f'Region{i}, City{i}, Street{i}, apartments{i}.')
            product = Product(name=f'Product{i}', description=f'Description{i}', price=randint(550, 100_000) * 0.01,
                              quantity=randint(1, 834))
            user.save()
            product.save()
