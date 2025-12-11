from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    passport_number = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    extra_info = models.TextField()

    def __str__(self):
        return self.username
