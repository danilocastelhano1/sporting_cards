from django.db import models


# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=30, null=False, blank=False)


class Card(BaseModel):
    texto = models.TextField(null=False, blank=False)
    tags = models.ManyToManyField(Tag, null=False, blank=False, related_name='card_tags')
