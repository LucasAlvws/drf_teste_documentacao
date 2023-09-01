from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse 
from rest_framework import status

class AthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_atenticacao_ser_com_credenciais_corretas(self):
        user = authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_auth(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_requisicao_get_user_errado(self):
        user = authenticate(username='c3oo', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)