from rest_framework import viewsets
from nexus_app.api.serializers.interview import InterviewSerializer
from nexus_app.models import Interview
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class InterviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
