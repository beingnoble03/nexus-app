from rest_framework import serializers
from nexus_app.models import Score


class ScoreSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = Score