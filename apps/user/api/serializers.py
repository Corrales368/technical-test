# Import django
from rest_framework import serializers

# Import self app
from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user model class
    """
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
        ]
    