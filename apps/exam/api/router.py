# Import django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import self app
from apps.exam.api import viewsets


router = DefaultRouter()

router.register('exam', viewsets.ExamModelViewSet , basename='exam')
router.register('question', viewsets.QuestionModelViewSet, basename='question')
router.register('answer', viewsets.AnswerModelViewSet, basename='answer')
router.register('answer-student',viewsets.AnswerStudentModelViewSet, basename='answer-student')

urlpatterns = [
    path('api/v1/exam/', include(router.urls))
]