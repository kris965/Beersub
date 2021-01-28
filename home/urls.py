from django.urls import path
from . views import (
    products,
    checkout,
    home
)

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('checkout/templates/checkout.html', checkout, name='checkout'),
    path('products/templates/products.html', products, name='products')
]
