from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Deposit(models.Model):
    date = models.DateField(auto_now_add=True)
    periods = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    amount = models.IntegerField(
        validators=[MinValueValidator(10_000), MaxValueValidator(3_000_000)]
    )
    rate = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(8)])

    def __str__(self):
        return f"Deposit {self.id}: {self.amount} for {self.periods} days"
