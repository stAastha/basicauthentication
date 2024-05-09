
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import BasicAuthentication

class MovieViewSet(viewsets.ModelViewSet):
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = MovieModel.objects.all()
	serializer_class = MovieSerializer

class StudentViewSet(viewsets.ModelViewSet):
	queryset = StudentModel.objects.all()
	serializer_class = StudentSerializer
