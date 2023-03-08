# Import django
from rest_framework import serializers

# Import self app
from apps.student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the student model class
    """
    class Meta:
        model = Student
        fields = [
            'id',
            'gender',
            'user',
        ]

    