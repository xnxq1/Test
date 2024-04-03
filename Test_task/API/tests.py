from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.urls import include, path, reverse, reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

from API.models import Exercises, Type


class ApiTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test')
        self.type1 = Type.objects.create(id=1, name='Силовые')

        self.type2 = Type.objects.create(id=2, name='Кардио')
        self.exercise1 = Exercises.objects.create(
                                             id=1,
                                             name='Exercise 1',
                                             description='Description 1',
                                             type_id=1,
                                             difficult='Начинающий',
                                             number_of_repetitions=15,
                                             number_of_approaches=3,
                                             time=45)

        self.exercise2 = Exercises.objects.create(name='Exercise 2',
                                                  id=2,
                                             description='Description 2',
                                             type_id=2,
                                             difficult='Средний',
                                             number_of_repetitions=23,
                                             number_of_approaches=4,
                                             time=40)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_get_exercise_list(self):
        url = 'http://127.0.0.1:8000/exercises/'

        response_unauthorized = self.client.get(url, format='json')
        self.assertEqual(response_unauthorized.status_code, status.HTTP_401_UNAUTHORIZED)

        token = self.get_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response_authorized = self.client.get(url, format='json')
        self.assertEqual(response_authorized.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response_authorized.data) > 0, "Данные в ответе не пустые")


    def test_get_exercise_detail(self):
        url = 'http://127.0.0.1:8000/exercises/1/'

        token = self.get_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response_authorized = self.client.get(url, format='json')
        self.assertEqual(response_authorized.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response_authorized.data) != 0)

    def test_post_exercise(self):
        body = {
            "name": "Exercise3",
            "description": "Description3",
            "type": 1,
            "difficult": "Продвинутый",
            "number_of_repetitions": 45,
            "number_of_approaches": 3,
            "time": 40
        }

        url = 'http://127.0.0.1:8000/exercises/'

        token = self.get_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response_authorized = self.client.post(url, data=body, format='json')
        self.assertEqual(response_authorized.status_code, status.HTTP_201_CREATED)

    # def test_patch_exercise(self):
    #     body = {
    #         "name": "Exercise6"
    #     }
    #     url = 'http://127.0.0.1:8000/exercises/1'
    #     token = self.get_token(self.user)
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    #
    #     response_authorized = self.client.patch(url, data=body, format='json')
    #
    #     self.assertEqual(response_authorized.status_code, status.HTTP_301_MOVED_PERMANENTLY)
    #
    # def test_delete_exercise(self):
    #
    #     url = 'http://127.0.0.1:8000/exercises/2'
    #     token = self.get_token(self.user)
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    #
    #     response_authorized = self.client.delete(url, format='json')
    #
    #     self.assertEqual(response_authorized.status_code, status.HTTP_301_MOVED_PERMANENTLY)
