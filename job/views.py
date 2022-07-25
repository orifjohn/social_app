from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from helpers.pagination import CustomPagination


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="salary", lookup_expr='gte')
    max_price = filters.ChoiceFilter(field_name="salary", lookup_expr='lte')

    class Meta:
        model = Job
        fields = ['region', 'status']


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
