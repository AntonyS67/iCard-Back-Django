from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from tables.models import Table
from tables.api.serializer import TableSerializer

class TableApiViewSet(ModelViewSet):
    permissions_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number']