from rest_framework import viewsets
from nexus_app.models import Panel
from nexus_app.api.serializers.panel import PanelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class PanelViewSet(viewsets.ModelViewSet):
    """
    Gets the list of all panels, create, retrieve panel instances.
    Pass a list of 'members' when creating/ updating panel instance
    """
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = PanelSerializer
    queryset = Panel.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    search_fields = ['place', ]
    filterset_fields = ['available', 'status', ]
    ordering_fields = '__all__'