from django.db import models
from shortuuidfield import ShortUUIDField

# Create your models here.
class Customer(models.Model):
    id = ShortUUIDField(unique=True)
    first_name= models.CharField()
    last_name= models.CharField()
    associated_account=models.ForeignKey("Account")
