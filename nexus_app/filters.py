from django_filters import FilterSet
from django_filters.rest_framework import DateTimeFilter, CharFilter, BooleanFilter, NumberFilter
from .models import Interview
from django.db.models import DateTimeField


class InterviewDateAndTimeFilterSet(FilterSet):
    time_assigned_min = DateTimeFilter(field_name='time_assigned', lookup_expr='gte')
    time_assigned_max = DateTimeFilter(field_name='time_assigned', lookup_expr='lte')
    time_entered_min = DateTimeFilter(field_name='time_entered', lookup_expr='gte')
    time_entered_max = DateTimeFilter(field_name='time_entered', lookup_expr='lte')
    completed = BooleanFilter(field_name='completed', lookup_expr='exact')
    round = NumberFilter(field_name='round', lookup_expr='exact')

    class Meta:
        model = Interview
        fields = '__all__'