# Import django
from django.db import models
from django.contrib.auth import get_user_model


# Get user model from project
user = get_user_model()

class Student(models.Model):
    """
    Model to store students
    """
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user}'