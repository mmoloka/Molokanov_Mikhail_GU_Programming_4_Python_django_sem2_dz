from django.urls import path
from . import views


urlpatterns = [
    path('user/<int:user_id>/', views.get_orders, name='get_orders'),
    path('products/user/<int:user_id>/', views.get_products, name='get_products'),
    ]