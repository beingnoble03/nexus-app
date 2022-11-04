from pyexpat import model
from rest_framework import serializers
from nexus_app.models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if self.initial_data.get("action") == "add":
            for round in instance.round.all():
                validated_data["round"].append(round.id)
        elif self.initial_data.get("action") == "delete":
            rounds_to_be_removed = validated_data["round"]
            validated_data["round"] = []
            for round in instance.round.all():
                if not round in rounds_to_be_removed:
                    validated_data["round"].append(round.id)
        return super().update(instance, validated_data)