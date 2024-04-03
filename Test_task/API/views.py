from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from API.serializers import ExerciseSerializer
from API.models import Exercises

# Create your views here.


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercises.objects.all().prefetch_related('type')
    serializer_class = ExerciseSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        self.queryset = super().get_queryset()
        type = self.request.GET.get('type', None)
        difficult = self.request.GET.get('difficult', None)

        if type:
            self.queryset = self.queryset.filter(type_id__name=type)

        if difficult:
            self.queryset = self.queryset.filter(difficult=difficult)

        return self.queryset
