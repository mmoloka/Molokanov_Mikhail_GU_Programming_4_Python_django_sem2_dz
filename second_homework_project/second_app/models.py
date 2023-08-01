from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField(unique=True)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'User_name: {self.name}; email: {self.email}; phone: {self.phone}.'


class Product(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    add_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Product_name: {self.name}; price: {self.price}.'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    prducts = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Order_id: {self.pk}; order_price {self.total_price}'
