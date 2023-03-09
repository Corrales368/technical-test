# Import django
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Import project
from apps.shared.api import pagination # Pagination classes

# Import self app
from apps.student.models import Student 
from apps.student.api.serializers import StudentSerializer 


class StudentModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to perform CRUD operations on students
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = pagination.MediumPageNumberPagination
    