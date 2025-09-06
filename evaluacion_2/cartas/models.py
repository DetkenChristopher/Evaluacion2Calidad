from django.db import models

# Create your models here.

class Carta(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    defense = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    attribute = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    cardmarket_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
