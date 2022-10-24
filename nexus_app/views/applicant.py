from rest_framework import viewsets
from nexus_app.api.serializers.applicant import ApplicantSerializer
from nexus_app.models import Applicant
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ApplicantViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    search_fields = ['name', 'enrolment_number', ]
    ordering_fields = ['name', ]
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()