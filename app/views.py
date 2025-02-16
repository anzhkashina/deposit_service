from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import calculate_deposit
from .models import Deposit
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class DepositCalculationAPIView(APIView):
    def post(self, request):
        try:
            result = calculate_deposit(request.data)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, _, pk):
        try:
            deposit = Deposit.objects.get(pk=pk)
            return Response(deposit.final_amount, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(
                {"error": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND
            )
