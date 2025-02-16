import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Deposit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "periods",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(60),
                        ]
                    ),
                ),
                (
                    "amount",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(10000),
                            django.core.validators.MaxValueValidator(3000000),
                        ]
                    ),
                ),
                (
                    "rate",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(8),
                        ]
                    ),
                ),
            ],
        ),
    ]
