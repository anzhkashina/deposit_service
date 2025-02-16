from rest_framework import serializers
from .models import Deposit, models


class DepositSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    periods = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()
    rate = serializers.FloatField()
    final_amount = serializers.JSONField()

    class Meta:
        model = Deposit
        fields = ["date", "periods", "amount", "rate", "final_amount"]
