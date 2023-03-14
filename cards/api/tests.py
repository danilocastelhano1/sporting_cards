from rest_framework.test import APITestCase

from freezegun import freeze_time

from .models import Tag
from .models import Card


class TagTests(APITestCase):

    def test_create_a_tag(self):
        data = {
            "name": "test example"
        }

        resp = self.client.post("/api/tag/", data=data, format="json")
        self.assertEqual(resp.status_code, 201)

    def test_list_many_tag(self):
        Tag.objects.create(name="simple tag 1")
        Tag.objects.create(name="simple tag 2")
        Tag.objects.create(name="simple tag 3")

        resp = self.client.get("/api/tag/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)

    def test_read_one_tag(self):
        tag = Tag.objects.create(name="simple tag 1")

        resp = self.client.get("/api/tag/{}/".format(tag.id))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"id": 1, "name": "simple tag 1"})

    def test_update_one_tag(self):
        tag = Tag.objects.create(name="simple tag 1")

        resp = self.client.patch("/api/tag/{}/".format(tag.id), data={"name": "update tag"}, format="json")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"id": 1, "name": "update tag"})

    def test_delete_one_tag(self):
        tag = Tag.objects.create(name="simple tag 1")

        resp = self.client.delete("/api/tag/{}/".format(tag.id))

        self.assertEqual(resp.status_code, 204)


class CardsTests(APITestCase):

    def test_create_a_card(self):
        data = {
            "texto": "Text Example",
            "tags": [
                "Politica",
                "Mundo"
            ]
        }

        resp = self.client.post("/api/card/", data=data, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()["tags"], ["Politica", "Mundo"])

    def test_list_many_cards(self):
        tag = Tag.objects.create(name="simple tag")

        c1 = Card.objects.create(texto="simple text 2")
        c1.tags.add(tag)

        c2 = Card.objects.create(texto="simple tag 2")
        c2.tags.add(tag)

        resp = self.client.get("/api/card/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 2)

    @freeze_time("2023-03-14 12:00:00")
    def test_read_one_card(self):
        tag = Tag.objects.create(name="simple tag 1")

        c1 = Card.objects.create(texto="simple text 2")
        c1.tags.add(tag)

        resp = self.client.get("/api/card/{}/".format(c1.id))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {
            "id": 1,
            "texto": "simple text 2",
            "data_criacao": "2023-03-14T12:00:00Z",
            "data_modificacao": "2023-03-14T12:00:00Z",
            "tags": [
                "simple tag 1"
            ]
        })

    @freeze_time("2023-03-14 15:00:00")
    def test_update_one_card(self):
        tag = Tag.objects.create(name="simple tag 1")

        c1 = Card.objects.create(texto="simple Update")
        c1.tags.add(tag)

        resp = self.client.patch("/api/card/{}/".format(c1.id),
                                 data={"texto": "New Update Value", "tags":["test1", "test2"]},
                                 format="json")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {
            "id": 1,
            "texto": "New Update Value",
            "data_criacao": "2023-03-14T15:00:00Z",
            "data_modificacao": "2023-03-14T15:00:00Z",
            "tags": [
                "test1", "test2"
            ]
        })

    def test_delete_one_card(self):
        tag = Tag.objects.create(name="simple tag 1")

        c1 = Card.objects.create(texto="simple Delete")
        c1.tags.add(tag)

        resp = self.client.delete("/api/card/{}/".format(c1.id))

        self.assertEqual(resp.status_code, 204)
