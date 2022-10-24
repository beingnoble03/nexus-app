from rest_framework import viewsets
from nexus_app.api.serializers.section import SectionSerializer
from nexus_app.models import Section
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


class SectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ] 
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, ]
    search_fields = ['title', ]
    ordering_fields = '__all__'
    serializer_class = SectionSerializer
    queryset = Section.objects.all()