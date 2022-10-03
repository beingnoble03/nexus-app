from rest_framework import viewsets
from nexus_app.models import InterviewSection
from nexus_app.api.serializers.interview_section import InterviewSectionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class InterviewSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = InterviewSectionSerializer
    queryset = InterviewSection.objects.all()