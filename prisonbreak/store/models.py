from django.db import models
from django.utils import timezone


class Item(models.Model):
    title = models.CharField(max_length=150)
    season = models.CharField(max_length=150)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    stock = models.IntegerField(default=0)
