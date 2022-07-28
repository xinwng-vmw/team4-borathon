from django.db import models
from shortuuidfield import ShortUUIDField
# Create your models here.


class Transaction(models.Model):
    transaction_id = ShortUUIDField(unique=True)
    amount = models.FloatField(default=0.00)
    type = models.BinaryField()  # 0 for Credit, 1 for Debit

    associated_account = models.ForeignKey(
        "Account", on_delete=models.SET_NULL)
    # not too sure about the foreign key
