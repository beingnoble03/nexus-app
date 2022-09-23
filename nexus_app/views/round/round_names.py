from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from nexus_app.api.serializers.round import RoundNameSerializer
from nexus_app.models import Round


class RoundNameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RoundNameSerializer
    queryset = Round.objects.all()