from rest_framework import viewsets
from nexus_app.api.serializers.section_marks import SectionMarksSerializer
from nexus_app.models import SectionMarks


class SectionMarksViewSet(viewsets.ModelViewSet):
    serializer_class = SectionMarksSerializer
    queryset = SectionMarks.objects.all()