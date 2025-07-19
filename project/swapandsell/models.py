from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import User

class Product(models.Model):

    class SaleType(models.TextChoices):
        SWAP = 'SWAP', 'Swap'
        SELL = 'SELL', 'Sell'

    class Condition(models.TextChoices):
        NEW = 'NEW', 'New'
        USED = 'USED', 'Used'
        DAMAGED = 'DAMAGED', 'Damaged'
    
    class ProductType(models.TextChoices):
        IPHONE = "iPhone"
        ANDROID = "Android"
        LAPTOP = "Laptop"

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    condition = models.CharField(
        max_length=10,
        choices=Condition.choices,
        default=Condition.NEW
    )
    sale_type = models.CharField(
        max_length=10,
        choices=SaleType.choices,
        default=SaleType.SWAP
    )
    product_type = models.CharField(
        max_length=20,
        choices=ProductType.choices,
        default=ProductType.IPHONE
    )
    price = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=255, default="Set an Address")
    photo_of_product = models.ImageField(null=True, blank=True)
    another_photo = models.ImageField(null=True, blank=True)
    listing_date = models.DateTimeField(default=now)
    contact_number = models.CharField(null=True, blank=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
