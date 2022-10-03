from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from nexus_app.api.serializers.test import TestApplicantSerializer
from nexus_app.models import Test
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class TestApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ] 
    serializer_class = TestApplicantSerializer
    queryset = Test.objects.all()

# merge with other test_ files into a single viewset.