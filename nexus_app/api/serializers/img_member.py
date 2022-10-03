from rest_framework import serializers
from nexus_app.models import ImgMember


class ImgMemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "enrolment_number", "name", "username", "year", "email"]
        model = ImgMember

class ImgMemberNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "name"]
        model = ImgMember