from rest_framework import viewsets
from nexus_app.api.serializers.season import SeasonSerializer
from nexus_app.models import Season
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class SeasonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ] 
    serializer_class = SeasonSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name', 'role', ]
    queryset = Season.objects.all()