from nexus_app.models import Interview
from rest_framework import serializers

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview