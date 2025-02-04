import pytest
from django.test import TestCase


@pytest.mark.django_db
class DepositTests(TestCase):
    ...

    def test_something(self):
        assert True
