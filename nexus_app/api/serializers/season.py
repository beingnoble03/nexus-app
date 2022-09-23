from rest_framework import serializers
from nexus_app.models import Season


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Season