from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from nexus_app.api.serializers.img_member import ImgMemberNameSerializer
from nexus_app.models import ImgMember
from nexus_app.api.serializers.img_member import ImgMemberSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from nexus_app.permissions import CanViewMemberDetails
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
import requests
import string
import random

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CanViewMemberDetails]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = ImgMemberSerializer
    queryset = ImgMember.objects.all()

    # permission_classes_by_action = {
    #     'update': PermissionUpdateClass,

    # }
    # def get_permissions(self):
    #     if self.action == 'update':
    #         self.permission_classes_by_action[self]
    @action(
        methods=["POST", "GET", ],
        detail=False,
        url_path="onLogin",
        url_name="onLogin",
        permission_classes = [AllowAny, ]
    )
    def on_login(self, request):
        data = {
        "client_id": "i8VvoKOswXhwAUA4KrjbpBsj87CrFgreBLhN1IgE",
        "client_secret": "c0Tkra7lexDUCO1RhCyuJbskRUNkZVP3X4daqP90yBuEbN2WqnUpw1EUWlxAR2rKtLlIeP0r00n0RiIU6gOMR2X9KJM7WEjZ7CkYEr3YzHgAG4kJjQAvvNmKMcfYczIM",
        "grant_type": "authorization_code",
        "redirect_uri": "http://localhost:8000/api/members/onLogin",
        "code": request.GET["code"]
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

        if "error" in user_data.keys():
            return Response(user_data, status=status.HTTP_400_BAD_REQUEST)
        else:
            student_details = user_data["student"]
            contact_details = user_data["contactInformation"]
            social_details = user_data["socialInformation"]
            personal_details = user_data["person"]
            try:
                user_required = ImgMember.objects.get(
                    username = user_data["username"])
            except ImgMember.DoesNotExist:
                choice_letters = string.ascii_letters + string.digits + string.punctuation
                random_password = ''.join(random.choice(choice_letters)
                for i in range(16))

                user_username = user_data["username"]
                user_password = make_password(random_password)
                user_name = personal_details["fullName"]
                user_branch = student_details["branch name"]
                user_year = student_details["currentYear"]
                user_enrolment_number = student_details["enrolmentNumber"]
                user_email = contact_details["instituteWebmailAddress"]
                user_image = "https://channeli.in" + personal_details["displayPicture"]

                is_maintainer = False
                roles = personal_details["roles"]
                for role in roles:
                    if role["role"] == "Maintainer":
                        is_maintainer = True

                if not is_maintainer:
                    return Response({
                        "error": "Only IMGians can access this portal."
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                img_member = ImgMember(
                    username = user_username,
                    name = user_name,
                    password = user_password,
                    branch = user_branch,
                    year = user_year,
                    enrolment_number = user_enrolment_number,
                    email = user_email,
                    image = user_image
                )
                img_member.is_staff = True
                img_member.save()
                user_data["token"] = Token.objects.get(user = img_member).key
                return Response(user_data, status=status.HTTP_201_CREATED)

            user_required.name = personal_details["fullName"]
            user_required.branch = student_details["branch name"]
            user_required.year = student_details["currentYear"]
            user_required.enrolment_number = student_details["enrolmentNumber"]
            user_required.email = contact_details["instituteWebmailAddress"]
            user_required.image = "https://channeli.in" + personal_details["displayPicture"]
            user_required.save()
            user_data["token"] = Token.objects.get(user = user_required).key
            return redirect(f'http://localhost:3000/oauthJump/?token={user_data["token"]}')


    @action(
        methods=['GET', ],
        detail=True,
        url_path='name',
        url_name='name',
        permission_classes = [IsAuthenticated, ],
        authentication_classes = [TokenAuthentication, ],
    )
    def get_names(self, request, pk = None):
        img_member = get_object_or_404(ImgMember, pk = pk)
        serializer = ImgMemberNameSerializer(img_member)
        return Response(serializer.data, status.HTTP_200_OK)

    @action(
        methods=['GET', ],
        detail=False,
        url_name='namesListNot2y',
        url_path='namesListNot2y',
        permission_classes = [IsAuthenticated, ],
        authentication_classes = [TokenAuthentication, ]
    )
    def get_names_list(self, request):
        serializer = ImgMemberNameSerializer(ImgMember.objects.filter(~Q(year=2) & ~Q(year=1)), many = True)
        return Response(serializer.data, status.HTTP_200_OK)