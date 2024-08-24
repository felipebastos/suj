from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from sujauth.models import User
from sujauth.serializers import UserSerializer

from django.shortcuts import render

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().exclude(is_active=False)

    serializer_class = UserSerializer

    permission_classes = [DjangoModelPermissions]
    

def activate_user(request, uid, token):
    return render(request, 'sujauth/activate.html', context={'uid':uid, 'token':token})
