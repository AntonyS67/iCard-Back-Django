from rest_framework.viewsets import ModelViewSet
# Los autenticados pueden ahcer todo sino solo pueden leer
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from categories.models import Category
from categories.api.serializers import CategorySerializer

class CategoryApiViewSet(ModelViewSet):
    permissions_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()