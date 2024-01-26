from django.db import models
from django.conf import settings

# Create your models here.
class ProductModel(models.Model):
    title = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        blank = True,
        null = True
    )
    color = models.TextField()
    product_dimensions = models.TextField()