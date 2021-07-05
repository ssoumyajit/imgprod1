from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]


class User(AbstractUser):
    # no need to inherit email because it is there in AbstractUser
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
