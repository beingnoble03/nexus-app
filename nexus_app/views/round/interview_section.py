from rest_framework import viewsets
from nexus_app.models import InterviewSection
from nexus_app.api.serializers.interview_section import InterviewSectionSerializer


class InterviewSectionViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSectionSerializer
    queryset = InterviewSection.objects.all()