from rest_framework import serializers
from nexus_app.models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Score