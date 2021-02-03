from django.urls import path
from .views import ItemDetailView


app_name = "products"

urlpatterns = [
    path('<slug:slug>', ItemDetailView.as_view(), name='products')
]
