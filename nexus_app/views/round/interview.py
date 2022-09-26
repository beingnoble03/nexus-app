from rest_framework import viewsets
from nexus_app.api.serializers.interview import InterviewSerializer
from nexus_app.models import Interview


class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
