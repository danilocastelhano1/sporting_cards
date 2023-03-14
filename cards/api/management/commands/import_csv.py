import csv

from typing import List

from django.core.management.base import BaseCommand
from django.db import transaction

from cards.api.models import Tag
from cards.api.models import Card


class Command(BaseCommand):
    help = "Seed the database informations"

    def add_arguments(self, parser):
        parser.add_argument('--csv_file', type=str, help='Caminho + arquivo do CSV)')

    @transaction.atomic
    def handle(self, *args, **kwargs):
        csv_file: str = kwargs['csv_file']

        try:
            with open(csv_file, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                next(reader, None)

                self.stdout.write(
                    self.style.SUCCESS("Lendo o CSV: {}".format(csv_file))
                )

                for row in reader:
                    card_text: str = row[0]
                    card_tags: str = row[1]

                    self.stdout.write(
                        self.style.SUCCESS("Lendo o texto: {}, tags: {}".format(card_text, card_tags))
                    )

                    created_tags: List[Tag] = []
                    if card_tags:
                        for tag in card_tags.split(";"):
                            filtered_tag = Tag.objects.filter(name=tag)
                            if filtered_tag.count() == 0:
                                created_tags.append(Tag.objects.create(name=tag))
                            else:
                                created_tags.append(filtered_tag.first())

                    if card_text:
                        filtered_card = Card.objects.filter(texto=card_text)
                        if filtered_card.count() == 0:
                            filtered_card = Card.objects.create(texto=card_text)
                        else:
                            filtered_card = filtered_card.first()
                        for created_tag in created_tags:
                            filtered_card.tags.add(created_tag)
                        filtered_card.save()

                self.stdout.write(
                    self.style.SUCCESS("Processo finalizado com Sucesso!")
                )
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR("Arquivo não encontrado!")
            )
        except Exception as err:
            self.stdout.write(
                self.style.ERROR("Erro ao Adicionar os valores do CSV no Banco, {}".format(err))
            )
