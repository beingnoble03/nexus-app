from rest_framework import viewsets
from nexus_app.api.serializers.applicant import ApplicantSerializer
from nexus_app.models import Applicant


class ApplicantViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()