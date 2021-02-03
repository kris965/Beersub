from django.db import models
from django.shortcuts import reverse
# Create your models here.


def get_absolute_url(self):
    return reverse("products:product", kwargs={
        'slug': self.slug
    })
