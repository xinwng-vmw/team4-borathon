from django.db import models
from shortuuidfield import ShortUUIDField

# Create your models here.
class Customer(models.Model):
    customer_id = ShortUUIDField(unique=True)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    associated_account=models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
