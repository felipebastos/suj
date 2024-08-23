from django.urls import path, include
from rest_framework.routers import DefaultRouter

from sujauth.views import UserViewSet, activate_user

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('activate/<uid>/<token>/', activate_user),
]