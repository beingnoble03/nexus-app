from rest_framework import serializers
from nexus_app.models import ImgMember


class ImgMemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "enrollment_number", "first_name", "username", "year", "email"]
        model = ImgMember