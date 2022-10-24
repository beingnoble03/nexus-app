from rest_framework import viewsets
from nexus_app.api.serializers.interview import InterviewSerializer
from nexus_app.models import Interview
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import InterviewDateAndTimeFilterSet


class InterviewViewSet(viewsets.ModelViewSet):
    """
    A Model ViewSet for Interviews. Search Fields include Applicant Name, 
    Panel Place, Applicant Enrolment Number. Filtering queryset can be done
    passing 'completed' as a parameter and Ordering can be done based on any
    field. For example,
    '/api/interviews/?search=Noble&ordering=time_assigned&completed=true'
    is a sample url.
    """
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend, ]
    filterset_class = InterviewDateAndTimeFilterSet
    search_fields = ['applicant__name', 'panel__place',
                     'applicant__enrolment_number', ]
    ordering_fields = '__all__'
