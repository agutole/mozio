from languages.fields import LanguageField
from djmoney.models.fields import MoneyField

from django.db import models
from django.contrib.gis.db.models import PolygonField


class Provider(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    telphone = models.CharField(max_length=80)
    language = LanguageField()
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.name} ({self.email})'


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = MoneyField(decimal_places=3, max_digits=8)
    area = PolygonField()

    def __str__(self):
        return f'{self.name} ({self.price})'
