from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from nexus_app.api.serializers.season import SeasonSerializer
from nexus_app.models.season import Season


class SeasonViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()