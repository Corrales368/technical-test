# Import django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import self app
from apps.user.api.viewsets import UserModelViewSet


router = DefaultRouter()

router.register('',UserModelViewSet)

urlpatterns = [
    path('api/v1/users/', include(router.urls))
]