import json

from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .api.serializers import ProfileSerializer, ProfileStatusSerializer
from .models import Profile, ProfileStatus


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'testcase', 'email': 'testecase@teste.com.br',
                'password1': 'A_strong_password', 'password2': 'A_strong_password'}

        response = self.client.post('/api/rest-auth/registration/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    list_url = reverse('profile-list')

    def setUp(self):
        self.user = User.objects.create_user(
            username='davinci',
            password='A_strong_password')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(
            reverse('profile-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'davinci')

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse(
            'profile-detail', kwargs={'pk': 1}), data={'city': 'Anchiano', 'bio': 'Some Guy'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {'id': 1, 'user': 'davinci', 'bio': 'Some Guy', 'city': 'Anchiano', 'avatar': None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(
            username='somerandom', password='someRandom123123')
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse(
            'profile-detail', kwargs={'pk': 1}), data={'city': 'Anchiano', 'bio': 'hacked!!!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProfileStatusViewSetTestCase(APITestCase):

    url = reverse('status-list')

    def setUp(self):
        self.user = User.objects.create_user(
            username='davinci',
            password='A_strong_password')
        self.status = ProfileStatus.objects.create(
            user_profile=self.user.profile, status_content='status_test')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

    def test_status_list_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_create(self):
        data = {'status_content': 'a new status'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_profile'], 'davinci')
        self.assertEqual(response.data['status_content'], 'a new status')

    def test_single_status_retrieve(self):
        serializer_data = ProfileStatusSerializer(instance=self.status).data
        response = self.client.get(reverse('status-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_status_update_owner(self):
        data = {'status_content': 'content updated'}
        response = self.client.put(
            reverse('status-detail', kwargs={'pk': 1}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status_content'], 'content updated')

    def test_status_update_by_random_user(self):
        random_user = User.objects.create_user(
            username='somerandom', password='someRandom123123')
        self.client.force_authenticate(user=random_user)
        data = {'status_content': 'hacked!!!'}
        response = self.client.put(
            reverse('status-detail', kwargs={'pk': 1}), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
