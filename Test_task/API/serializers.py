from rest_framework import serializers

from API.models import Exercises


class ExerciseSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', read_only=True)
    class Meta:
        model = Exercises
        fields = ('id', 'name', 'description', 'difficult',
                  'number_of_repetitions', 'number_of_approaches', 'time', 'type')
