from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Koszyk(models.Model):
    name = models.CharField(max_length=255)


class Produkt(models.Model):
    nazwa = models.CharField(max_length=255)


class ZawartoscKoszyka(models.Model):
    koszyk = models.ForeignKey(Koszyk, on_delete=CASCADE, related_name='zawartosc')
    produkt = models.ForeignKey(Produkt, on_delete=CASCADE)
    liczba = models.IntegerField()
