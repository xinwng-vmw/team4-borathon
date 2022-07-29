from django.db import models
from shortuuidfield import ShortUUIDField

# Create your models here.


class Account(models.Model):
    id = ShortUUIDField(unique=True, primary_key=True)
    account_number = ShortUUIDField(unique=True)
    balance = models.FloatField(default=0.00)
    account_status = models.BooleanField()
