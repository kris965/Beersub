from django.shortcuts import render
from django.views.generic import DetailView
from home.models import Item


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "products/product.html"
