from urllib import request
from rest_framework import viewsets, status
from nexus_app.api.serializers.test import TestSectionSerializer
from nexus_app.api.serializers.section import SectionSerializer
from nexus_app. models import Test, Section
from rest_framework.response import Response

class TestSectionViewset(viewsets.ModelViewSet):
    """
    Returns sections with their questions of a test
    """
    serializer_class = TestSectionSerializer
    queryset = Test.objects.all()

    def create(self, request):
        request_data = request.data
        serialized_data = SectionSerializer(data = request_data)
        if serialized_data.is_valid():
            self.perform_create(serialized_data)
            return Response(serialized_data.data, status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.error_messages,
             status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serialized_data):
        serialized_data.save()