from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField

# Create your models here.
class Account(models.Model):
    account_id = ShortUUIDField(unique=True)
    account_number = ShortUUIDField(unique=True)
    balance = models.FloatField(default=0.00)
    account_status = models.BinaryField()