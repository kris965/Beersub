
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls', namespace='home')),
    path('products/', include('products.urls')),
    path('checkout/', include('checkout.urls')),
]
