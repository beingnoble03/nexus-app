from rest_framework import viewsets
from nexus_app.api.serializers.applicant import ApplicantSerializer
from nexus_app.models import Applicant
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ApplicantViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()