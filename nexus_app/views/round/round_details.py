from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from nexus_app.api.serializers.round import RoundSerializer
from nexus_app.models import Round


class RoundViewset(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    queryset = Round.objects.all()