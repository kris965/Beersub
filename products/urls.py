from django.urls import path
from .views import ItemDetailView

urlpatterns = [
    path('<slug:slug>', ItemDetailView.as_view(), name='product-detail')
]
