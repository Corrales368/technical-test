# Import django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import self app
from apps.student.api.viewsets import StudentModelViewSet


router = DefaultRouter()

router.register('',StudentModelViewSet)

urlpatterns = [
    path('api/v1/students/', include(router.urls))
]