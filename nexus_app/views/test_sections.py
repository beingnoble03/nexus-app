from urllib import request
from rest_framework import viewsets, status
from nexus_app.api.serializers.test import TestSectionSerializer
from nexus_app.api.serializers.section import SectionSerializer
from nexus_app. models import Test, Section
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class TestSectionViewset(viewsets.ModelViewSet):
    """
    Returns sections with their questions of a test
    """
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]  
    serializer_class = TestSectionSerializer
    queryset = Test.objects.all()

    def create(self, request):
        request_data = request.data
        serializer = SectionSerializer(data = request_data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages,
             status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()