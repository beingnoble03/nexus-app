from rest_framework import serializers
from nexus_app.models import SectionMarks


class SectionMarksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SectionMarks