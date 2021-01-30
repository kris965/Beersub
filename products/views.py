from django.shortcuts import render
from home.models import Item


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)