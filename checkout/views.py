from django.shortcuts import render
from .views import checkout


def checkout(request):
    return render(request, 'checkout/checkout.html')
