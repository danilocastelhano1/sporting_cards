from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Tag
from .models import Card

from .serializers import TagSerializer
from .serializers import CardSerializer



class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class CardViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [AllowAny]
