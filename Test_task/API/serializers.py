from rest_framework import serializers

from API.models import Exercises


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercises
        fields ='__all__'


