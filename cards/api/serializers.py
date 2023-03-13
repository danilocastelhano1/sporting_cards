from rest_framework import serializers
from .models import Tag
from .models import Card


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name",)
        read_only_fields = ("id", "data_criacao", "data_modificacao")


class CardSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Card
        fields = ("id", "texto", "data_criacao", "data_modificacao", "tags")
        read_only_fields = ("id", "data_criacao", "data_modificacao")
