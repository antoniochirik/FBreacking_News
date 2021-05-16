import json

from django.test import Client, TestCase
from django.urls import reverse

from Users.models import User

# Пока не отстроено взаимодействие с базой Postgres


USERNAME = 'user1'
SUPERUSERNAME = 'admin'
PASSWORD='1234'
USERS_URL = reverse('all_profiles')
AUTH_URL = reverse('token_obtain_pair')
REFRESH_URL = reverse('token_refresh')


class UserURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.admin = User.objects.create_superuser(
            username=SUPERUSERNAME,
            password=PASSWORD
        )

    def setUp(self):
        self.user_data = {
            'username': USERNAME,
            'password': PASSWORD
        }
        self.invalid_user_data = {
            'username': '',
            'password': PASSWORD
        }
        self.guest_client = Client()
        self.admin_client = Client()
        self.admin_client.force_login(self.admin)

    def test_create_valid_user(self):
        response = self.guest_client.post(
            USERS_URL,
            data=json.dumps(self.user_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_create_invalid_user(self):
        response = self.guest_client.post(
            USERS_URL,
            data=json.dumps(self.invalid_user_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_getting_token_for_users(self):
        """
        Страница авторизации отдает токен пользователям
        с корректными данными
        """
        response = self.guest_client.post(
            AUTH_URL,
            data={
                'username': USERNAME,
                'password': PASSWORD
            }
        )
        self.assertEqual(response.status_code, 200)
