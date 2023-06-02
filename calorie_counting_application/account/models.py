from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MALE = "M"
FEMALE = "F"
GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
]


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    