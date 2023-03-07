# Import django
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Model to store users
    """
    email = models.EmailField(unique=True)
    
    def __str__(self) -> str:
        return self.username