from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    aadhaar_encrypted = models.TextField(null=True, blank=True)
