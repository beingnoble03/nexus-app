from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from nexus_app.models import ImgMember
from nexus_app.api.serializers.img_member import ImgMemberSerializer
import requests

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = ImgMemberSerializer
    queryset = ImgMember.objects.all()

    @action(
        methods=["POST"],
        detail=False,
        url_path="onLogin",
        url_name="onLogin"
    )
    def on_login(self, request):
        data = {
        "client_id": "i8VvoKOswXhwAUA4KrjbpBsj87CrFgreBLhN1IgE",
        "client_secret": "c0Tkra7lexDUCO1RhCyuJbskRUNkZVP3X4daqP90yBuEbN2WqnUpw1EUWlxAR2rKtLlIeP0r00n0RiIU6gOMR2X9KJM7WEjZ7CkYEr3YzHgAG4kJjQAvvNmKMcfYczIM",
        "grant_type": "authorization_code",
        "redirect_uri": "http://localhost:3000/",
        "code": self.request.data["code"]
        }
        response_data = requests.post(
            url="https://channeli.in/open_auth/token/",
            data=data,
        ).json()
        user_data = requests.get(
            url= "https://channeli.in/open_auth/get_user_data/",
            headers={
                "Authorization": "Bearer " + response_data["access_token"]
            }
        ).json()
        if user_data["errors"]:
            return Response(user_data, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            member = ImgMember.objects.filter(
                enrollment_number = user_data.student.enrollmentNumber)
        except ImgMember.DoesNotExist:
            pass
        return Response(user_data, status=status.HTTP_200_OK)


        