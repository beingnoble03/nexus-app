from rest_framework import viewsets
from nexus_app.api.serializers.section_marks import SectionMarksSerializer
from nexus_app.models import SectionMarks
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class SectionMarksViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ] 
    serializer_class = SectionMarksSerializer
    queryset = SectionMarks.objects.all()