from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = "/api/create/"
PROFILE_URL = "/api/profile/"
TOKEN_URL = "/api/auth/"


class AuthorizedUserApiTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="dummy", password="dummy_pw")
