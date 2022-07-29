from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction  # this is the model that is being serialized
        fields = ('transaction_id', 'amount', 'type', 'associated_account')
