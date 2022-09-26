from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from nexus_app.api.serializers.test import TestApplicantSerializer
from nexus_app.models import Test


class TestApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TestApplicantSerializer
    queryset = Test.objects.all()