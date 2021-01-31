from django.conf import settings
from django.db import models

CATEGORY_CHOICES = (
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


LABEL_COLORS = (
    ('O', 'orange'),
    ('B', 'brown'),
    ('Y', 'yellow')
)


# Displays items available for purchase in the store #
class Item(models.Model):
    title = models.CharField(max_length=100)
    brewer = models.FloatField()
    style = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    label = models.CharField(choices=LABEL_COLORS, max_length=1)

    def __str__(self):
        return self.title


# Items added to the cart will become OrderItem #
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


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
