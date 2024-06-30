from unittest import TestCase

from django.db.migrations import serializer
from rest_framework.test import APITestCase

from module.models import Module
from module.validators import YoutubeValidator
from users.models import User
from django.urls import reverse
from rest_framework import status, serializers


class ModuleTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.pro",
            first_name="test1",
            last_name="testov",
            password="123qwe",
            is_active=True,
            is_staff=True,
        )
        self.user.set_password("123qwe")
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.module = Module.objects.create(
            owner=self.user,
            number=8,
            name="Общая теория относительности",
            description="Необходимость модификации ньютоновской теории гравитации."
        )

    def test_module_create(self):
        url = reverse("module:module-create")
        data = {
            "owner": self.user.pk,
            "number": 8,
            "name": "Общая теория относительности",
            "description": "Необходимость модификации ньютоновской теории гравитации."
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_module_retrieve(self):
        url = reverse("module:module-retrieve")
        data = {
            "owner": self.user.pk,
            "number": 8,
            "name": "Общая теория относительности",
            "description": "Необходимость модификации ньютоновской теории гравитации."
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_module_list(self):
        url = reverse("module:module-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.module.pk,
                    "owner": self.user.pk,
                    "number": 8,
                    "name": "Общая теория относительности",
                    "description": "Необходимость модификации ньютоновской теории гравитации."
                }, ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_module_update(self):
        url = reverse("module:module-update", args=(self.module.pk,))
        data = {
            "owner": self.user.pk,
            "number": 8,
            "name": "test",
            "description": "test"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_module_delete(self):
        url = reverse("module:module-delete", args=(self.module.pk,))
        data = {
            "owner": self.user.pk,
            "number": 8,
            "name": "test",
            "description": "test"
        }
        response = self.client.delete(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Module.objects.all().count(), 0)


class ValidatorTestCase(TestCase):
    def test_youtube_validator(self):
        youtube_validator = YoutubeValidator(field="video_url")

        with self.assertRaises(serializers.ValidationError) as context:
            youtube_validator({'video_url': 'https//www.words.com'})

        self.assertIn("Недопустимая ссылка на видео.", str(context.exception))

        try:
            youtube_validator({'video_url': 'https://www.youtube.com/watch?v=hcm55lU9knw'})
        except serializers.ValidationError:
            self.fail('youtube_validator raised ValidatorError unexpectedly!')
