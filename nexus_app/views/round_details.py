from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from nexus_app.api.serializers.round import RoundSerializer
from nexus_app.models import Round
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RoundViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = RoundSerializer
    queryset = Round.objects.all()