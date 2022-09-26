from nexus_app.models import Panel
from rest_framework import serializers
from .img_member import ImgMemberSerializer


class PanelSerializer(serializers.ModelSerializer):
    members_details = serializers.SerializerMethodField("get_members_details")

    def get_members_details(self, instance):
        return ImgMemberSerializer(instance.members, many = True).data

    class Meta:
        model = Panel
        fields = '__all__'