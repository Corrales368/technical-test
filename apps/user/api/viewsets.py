# Import django
from rest_framework import viewsets

# Import project
from apps.shared.api import pagination # Pagination classes

# Import self app
from apps.user.models import User 
from apps.user.api.serializers import UserSerializer 


class UserModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to perform CRUD operations on students
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = pagination.MediumPageNumberPagination