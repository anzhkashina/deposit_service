from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Deposit


class DepositAPITests(APITestCase):
    def setUp(self):
        self.deposit_data = {"amount": 1000, "term": 30, "interest_rate": 5}
        self.response = self.client.post("/deposits/", self.deposit_data, format="json")

    def test_create_deposit(self):
        self.assertEqual(Deposit.objects.count(), 1)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_deposit(self):
        response = self.client.get(f"/deposits/{Deposit.objects.first().id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "amount")
