from __future__ import unicode_literals

from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    # created_at
    # updated_at
    # is_published
    # created_by
    # updated_by
    # is_approved
    # approved_by


class City(models.Model):
    name = models.CharField(max_length=255)
    center_latitude = models.FloatField()
    center_longitude = models.FloatField()
