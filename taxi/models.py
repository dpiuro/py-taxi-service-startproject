from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="driver_set",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="driver_permissions_set", blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.license_number})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def __str__(self):
        return f"{self.model} ({self.manufacturer.name})"
