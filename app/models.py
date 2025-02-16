from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from app.services import calculate_deposit


class Deposit(models.Model):
    date = models.DateField()
    periods = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(10000), MaxValueValidator(3000000)]
    )
    rate = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    final_amount = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Вклад от {self.date}, на {self.periods} месяца(ев), сумма {self.amount}, ставка {self.rate}%"

    def save(self, *args, **kwargs):
        if not self.final_amount:
            self.final_amount = calculate_deposit(
                {
                    "date": self.date,
                    "periods": self.periods,
                    "amount": self.amount,
                    "rate": self.rate,
                }
            )
        super().save(*args, **kwargs)
