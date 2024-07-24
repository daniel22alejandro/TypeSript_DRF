from django.db import models
from django.contrib.auth.models import AbstractUser #registrar y autenticar usuarios


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

