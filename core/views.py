from django.shortcuts import render

from .models import User
from rest_framework.response import Response
from core.serializers import UserProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from core.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserProfileSerializer
    
    def get_permission(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action =='retrive' or self.action == 'update'or self.action =='':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return[permission() for permission in permission_classes]
# Create your views here.
