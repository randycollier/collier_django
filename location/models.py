# from django.db import models
from django.contrib.gis.db import models
# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=14)
    point = models.PointField(default='POINT(0.0 0.0)')
