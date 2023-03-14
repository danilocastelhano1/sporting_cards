from rest_framework import serializers
from .models import Tag
from .models import Card


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name",)
        read_only_fields = ("id", "data_criacao", "data_modificacao")


class CardSerializer(serializers.ModelSerializer):
    tags = serializers.ListSerializer(
        child=serializers.CharField(allow_blank=False))  # TagSerializer(many=True, read_only=False)

    class Meta:
        model = Card
        fields = ("id", "texto", "data_criacao", "data_modificacao", "tags")
        read_only_fields = ("id", "data_criacao", "data_modificacao")

    def create(self, validated_data):
        tags = validated_data.pop("tags")

        card = super(CardSerializer, self).create(validated_data)

        for tag in tags:
            tag_obj, created_tag = Tag.objects.get_or_create(name=tag, defaults={"name": tag})
            card.tags.add(tag_obj)

        return card

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags")

        card = super(CardSerializer, self).update(instance, validated_data)

        card.tags.all().delete()

        for tag in tags:
            tag_obj, created_tag = Tag.objects.get_or_create(name=tag, defaults={"name": tag})
            card.tags.add(tag_obj)

        return card
