from nexus_app.api.serializers.img_member import ImgMemberSerializer
from nexus_app.models import ImgMember
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CurrentUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = ImgMemberSerializer

    # 3y, 4y anything
    # can't view data of seniors
    # 2y can't view marks of this recruitment season

    def get_queryset(self):
        return ImgMember.objects.filter(username = self.request.user.username)