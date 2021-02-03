from django.conf import settings
from django.db import models
from django.shortcuts import reverse

STYLE_CHOICES = (
    ('APA', 'American Pale Ale'),
    ('IPA', 'Indian Pale Ale'),
    ('S', 'Stout'),
    ('WB', 'Wheat Beer'),
    ('PO', 'Porter'),
    ('BPA', 'Belgian Pale Ale'),
    ('B', 'Bock'),
    ('EPA', 'English Pale Ale'),
    ('P', 'Pilsner'),
    ('D', 'Dubbel'),
    ('T', 'Triple'),
    ('Q', 'Quadruple')
)

LABEL_COLOR_CHOICES = (
    ('Y', 'yellow'),
    ('DK', 'dark-yellow'),
    ('LO', 'ligh-torange'),
    ('A', 'amber'),
    ('LB', 'light-brown'),
    ('B', 'brown'),
    ('DB', 'dark-brown'),
    ('BK', 'black'),
)


# Displays items available for purchase in the store #
class Item(models.Model):
    name = models.CharField(max_length=100)
    brewer = models.CharField(max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, max_length=20)
    label = models.CharField(choices=LABEL_COLOR_CHOICES, max_length=2)
    percentage = models.FloatField(max_length=2)
    slug = models.SlugField()

    def __str__(self):
        return self.name


# Items added to the cart will become OrderItem #
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


# Used to store items user has added to their cart.#
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
