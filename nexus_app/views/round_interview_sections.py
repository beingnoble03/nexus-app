from rest_framework import viewsets
from nexus_app.api.serializers.round import RoundInterviewSectionSerializer
from nexus_app. models import Round
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RoundInterviewSectionViewSet(viewsets.ModelViewSet):
    """
    Get sections
    """
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]    
    serializer_class = RoundInterviewSectionSerializer
    queryset = Round.objects.filter(round_type = "I")