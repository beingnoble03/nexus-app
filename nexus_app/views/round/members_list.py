from rest_framework import viewsets
from nexus_app.models import ImgMember
from nexus_app.api.serializers.img_member import ImgMemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = ImgMemberSerializer
    queryset = ImgMember.objects.all()