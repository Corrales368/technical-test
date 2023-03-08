# Import django
from rest_framework import viewsets

# Import project
from apps.shared.api import pagination # Pagination classes

# Import self app
from apps.exam.models import (
    Exam,
    Question,
    Answer,
    AnswerStudent
)
from apps.exam.api.serializers import (
    ExamSerializer,
    QuestionSerializer,
    AnswerSerializer,
    AnswerStudentSerializer,
) 


class ExamModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to perform CRUD operations on exam
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    pagination_class = pagination.MediumPageNumberPagination


class QuestionModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to perform CRUD operations on question
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = pagination.MediumPageNumberPagination


class AnswerModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to perform CRUD operations on answer
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    pagination_class = pagination.MediumPageNumberPagination


class AnswerStudentModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to perform CRUD operations on students
    """
    queryset = AnswerStudent.objects.all()
    serializer_class = AnswerStudentSerializer
    pagination_class = pagination.MediumPageNumberPagination
    
    