from rest_framework import viewsets
from nexus_app.api.serializers.round import RoundInterviewSectionSerializer
from nexus_app. models import Round

class RoundInterviewSectionViewSet(viewsets.ModelViewSet):
    """
    Get sections
    """
    serializer_class = RoundInterviewSectionSerializer
    queryset = Round.objects.filter(round_type = "I")