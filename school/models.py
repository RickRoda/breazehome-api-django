
from django.db import models


class Schools(models.Model):
    zip_code = models.CharField(
        max_length=10,
        null=True
    )
    institution_name = models.CharField(
        max_length=80,
        null=True
    )
    street_address = models.CharField(
        max_length=60,
        null=True
    )
    city = models.CharField(
        max_length=60,
        null=True
    )
    state = models.CharField(
        max_length=2,
        null=True
    )
    type = models.CharField(
        max_length=20,
        null=True
    )
    grade_levels = models.CharField(
        max_length=20,
        null=True
    )
    phone = models.CharField(
        max_length=20,
        null=True
    )
    total_students = models.IntegerField(
        null=True
    )
    rank = models.IntegerField(
        null=True,
    )
    latitude = models.DecimalField(
        max_digits=12,
        decimal_places=5,
        null=True
    )
    longitude = models.DecimalField(
        max_digits=12,
        decimal_places=5,
        null=True
    )
