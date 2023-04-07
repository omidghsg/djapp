from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

TOKEN_URL = "/api/v1/token/"
TEST_USER_DATA = {"username": "testuser", "password": "testpassword"}


class TokenAPITest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(**TEST_USER_DATA)

    def test_get_token_success(self):
        """
        Ensure we can get a token with correct credentials
        """
        response = self.client.post(TOKEN_URL, TEST_USER_DATA, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
