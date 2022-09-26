from rest_framework import serializers
from nexus_app.models import InterviewSection

class InterviewSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSection
        fields = '__all__'