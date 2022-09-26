from rest_framework import viewsets
from nexus_app.models import Panel
from nexus_app.api.serializers.panel import PanelSerializer


class PanelViewSet(viewsets.ModelViewSet):
    """
    Gets the list of all panels, create, retrieve panel instances.
    Pass a list of 'members' when creating/ updating panel instance
    """
    serializer_class = PanelSerializer
    queryset = Panel.objects.all()