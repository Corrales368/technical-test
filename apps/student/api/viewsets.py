# Import django
from rest_framework import viewsets

# Import project
from apps.shared.api import pagination # Pagination classes

# Import self app
from apps.student.models import Student 
from apps.student.api.serializers import StudentSerializer 


class StudentModelViewSet(viewsets.ModelViewSet):
    """
    
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = pagination.MediumPageNumberPagination