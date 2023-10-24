from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK

from user.tests.dataset import user_valid_dataset


class PackageAuthentication(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("package-list")
        self.user = get_user_model().objects.create(
            **user_valid_dataset[0], is_active=True
        )

    def test_user_can_get_packages_without_login(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, HTTP_401_UNAUTHORIZED)

    def test_user_can_get_packages_after_login(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, HTTP_200_OK)
