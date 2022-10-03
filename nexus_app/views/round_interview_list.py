from django import views
from rest_framework import viewsets
from nexus_app.api.serializers.round import RoundInterviewListSerializer
from nexus_app.models import Round
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RoundInterviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = RoundInterviewListSerializer
    queryset = Round.objects.filter(round_type = "I")