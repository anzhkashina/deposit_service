import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_input_data(data):
    try:
        data["date"] = datetime.datetime.strptime(data["date"], "%d.%m.%Y").date()
    except ValueError:
        raise ValidationError(_("Неверный формат даты. Ожидается 'dd.mm.YYYY'."))

    if not isinstance(data["periods"], int) or not 1 <= data["periods"] <= 60:
        raise ValidationError(_("Периоды должны быть целым числом от 1 до 60."))

    if not isinstance(data["amount"], int) or not 10000 <= data["amount"] <= 3000000:
        raise ValidationError(
            _("Сумма должна быть целым числом от 10 000 до 3 000 000.")
        )

    if not isinstance(data["rate"], float) or not 1 <= data["rate"] <= 8:
        raise ValidationError(
            _("Ставка должна быть числом с плавающей точкой от 1 до 8.")
        )


def calculate_deposit(input_data):
    validate_input_data(input_data)

    result = {}
    current_date = input_data["date"]
    amount = input_data["amount"]
    monthly_interest_rate = input_data["rate"] / 12 / 100

    for i in range(input_data["periods"]):
        new_amount = amount * (1 + monthly_interest_rate)
        result[current_date.strftime("%d.%m.%Y")] = round(new_amount, 2)
        amount = new_amount
        current_date += datetime.timedelta(days=30)

    return result
