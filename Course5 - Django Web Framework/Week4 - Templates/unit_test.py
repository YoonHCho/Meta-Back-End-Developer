# models.py app level
from django.db import models

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name

# tests.py
from django.test import TestCase
from datetime import datetime
from .models import Reservation

class ReservationModelTest(TestCase):

    @classmethod # added after migration
    def setUpTestData(cls):
        cls.reservation = Reservation.object.create(
            first_name = "John",
            last_name = "McDonald"
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, str)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.booking_time, datetime)

'''
to run the test make and perform migrations, add @classmethod inside the class
run --> python manage.py test

'''