from django.conf import settings
from django.db import models

class Themes(models.Model):
    theme_name = models.CharField(
        max_length=200,
        unique=True
    )
    color_1 = models.CharField(
        max_length=7
    )
    color_2 = models.CharField(
        max_length=7
    )
    color_3 = models.CharField(
        max_length=7
    )
    color_4 = models.CharField(
        max_length=7
    )
    color_5 = models.CharField(
        max_length=7
    )
    color_6 = models.CharField(
        max_length=7
    )
    image = models.CharField(
        max_length=50
    )
    brand_font = models.CharField(
        max_length=100
    )
    is_deleted = models.BooleanField(
        default=False
    )

class Configuration(models.Model):
    system_theme = models.ForeignKey(
        'admins.Themes',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    google_api_key = models.CharField(
        max_length=200,
        default="AIzaSyCHa5mFbTGgyAABDm_d7M4msCk1LoF53tk"
    )
    polr_duration_max_tolerance = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        default=0.05
    )
    polr_search_angles = models.IntegerField(
        default=15
    )
    polr_search_iterations = models.IntegerField(
        default=32
    )
    polr_max_mpm = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        default=1.25
    )
    polr_google_matrix_elements_ps = models.IntegerField(
        default=50
    )



class PropertyFilter(models.Model):
    name = models.CharField(
        max_length=200
    )
    condition = models.CharField(
        max_length=500
    )
    order = models.IntegerField(
        default=1
    )
    active = models.BooleanField(
        default=False
    )
    trashed = models.BooleanField(
        default=False
    )
    locations = models.IntegerField(
        default=1
    )


