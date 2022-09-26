from django import views
from rest_framework import viewsets
from nexus_app.api.serializers.round import RoundInterviewListSerializer
from nexus_app.models import Round


class RoundInterviewViewSet(viewsets.ModelViewSet):
    serializer_class = RoundInterviewListSerializer
    queryset = Round.objects.filter(round_type = "I")