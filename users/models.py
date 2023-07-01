from django.db import models
from django.contrib.auth.models import AbstractUser


class UserChoices(models.TextChoices):
    STUDENT = ("student",)
    COLABORATOR = ("colaborator",)


class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=50, null=False)
    user_status = models.CharField(
        max_length=20,
        null=True,
        choices=UserChoices.choices,
        default=UserChoices.STUDENT,
    )
    pass
