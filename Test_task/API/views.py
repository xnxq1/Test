from django.shortcuts import render
from rest_framework import viewsets

from API.serializers import ExerciseSerializer
from API.models import Exercises

# Create your views here.


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = ExerciseSerializer
