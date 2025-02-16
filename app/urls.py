from django.urls import path
from .views import DepositCalculationAPIView

urlpatterns = [
    path(
        "api/deposits/", DepositCalculationAPIView.as_view(), name="deposit_calculation"
    ),
]
