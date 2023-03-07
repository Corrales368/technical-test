# Import django
from rest_framework import serializers

# Import self app
from apps.student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    
    """
    class Meta:
        model = Student
        fields = [
            'user'
        ]