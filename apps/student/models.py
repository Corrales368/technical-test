# Import django
from django.db import models
from django.contrib.auth import get_user_model


# Get user model from project
user = get_user_model()

class Student(models.Model):
    """
    Model to store students
    """
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user}'