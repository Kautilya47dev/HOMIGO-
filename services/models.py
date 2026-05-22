from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=15)

    address = models.TextField()

    def __str__(self):
        return self.customer_name


class AMCBooking(models.Model):

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    customer_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=15)

    address = models.TextField()

    appliance = models.CharField(max_length=100)

    timeline = models.CharField(max_length=50)

    selected_plan = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name