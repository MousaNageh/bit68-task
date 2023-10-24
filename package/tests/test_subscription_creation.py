from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from package.models import Package
from package.tests.dataset import valid_package_dataset
from user.tests.dataset import user_valid_dataset


class SubscriptionAuthorization(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("subscription-api")
        self.user = get_user_model().objects.create(
            **user_valid_dataset[0], is_active=True
        )
        self.client.force_authenticate(user=self.user)
        self.package_ids = self._create_packages()

    def test_create_subscriptions(self):
        res = self._send_post_request()
        self.assertEqual(res.status_code, HTTP_201_CREATED)
        res = self.client.get(self.url)
        self.assertEqual(len(valid_package_dataset), len(res.data.get("results")))

    def test_create_subscriptions_empty_packages_ids(self):
        res = self.client.post(self.url, data={"packages": []})
        self.assertEqual(res.status_code, HTTP_400_BAD_REQUEST)

    def test_create_subscriptions_for_packages_already_created(self):
        self._send_post_request()
        res = self._send_post_request()
        self.assertEqual(res.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("is already created", str(res.content))

    def test_create_subscriptions_for_packages_not_exits(self):
        res = self._send_post_request(packages=[43534543, 453453, 324234])
        self.assertEqual(res.status_code, HTTP_400_BAD_REQUEST)

    def _send_post_request(self, packages=None):
        data = {"packages": self.package_ids if not packages else packages}
        return self.client.post(self.url, data=data, format="json")

    @staticmethod
    def _create_packages():
        packages = Package.objects.bulk_create(
            [Package(**package) for package in valid_package_dataset]
        )
        return [package.id for package in packages]
