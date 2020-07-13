from django.db import models
from datetime import datetime


class Company(models.Model):
    name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=10, default="XXX")
    apz_rating = models.CharField(max_length=200)
    financial_rating = models.CharField(max_length=200)
    profitability_rating = models.CharField(max_length=200)
    def __str__(self):
        return self.name + " - symbol: " + str(self.api_key) + " - id: " + str(self.id)