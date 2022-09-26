from rest_framework import viewsets
from nexus_app.api.serializers.season import SeasonSerializer
from nexus_app.models import Season


class SeasonViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()