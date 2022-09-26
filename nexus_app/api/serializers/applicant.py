from pyexpat import model
from rest_framework import serializers
from nexus_app.models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'