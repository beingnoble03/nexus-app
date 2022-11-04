from rest_framework import serializers
from nexus_app.models import ImgMember


class ImgMemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "enrolment_number", "name", "username", "year", "email", "image", "is_master", "branch", ]
        model = ImgMember

class ImgMemberNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "name", "is_master", "image", ]
        model = ImgMember