from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(models.Model):
    fullname = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    job = models.CharField(max_length=128)
    salary = models.FloatField()
    position = models.CharField(max_length=128)
    address = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    social_media = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.fullname


