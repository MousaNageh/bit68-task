from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from package.models import Package
from package.tests.dataset import valid_package_dataset
from user.tests.dataset import user_valid_dataset
from package.queryset.subscription_queryset import SubscriptionQueryset


class SubscriptionAuthorization(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("subscription-api")
        self.user1 = get_user_model().objects.create(
            **user_valid_dataset[0], is_active=True
        )
        self.user2 = get_user_model().objects.create(
            **user_valid_dataset[1], is_active=True
        )
        self._create_subscriptions()

    def test_user_can_get_subscriptions_of_anther_user(self):
        self.client.force_authenticate(user=self.user2)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, HTTP_200_OK)
        self.assertFalse(len(res.data.get("results")))

    def test_user_can_get_subscriptions(self):
        self.client.force_authenticate(user=self.user1)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, HTTP_200_OK)
        self.assertEqual(len(valid_package_dataset), len(res.data.get("results")))

    def _create_subscriptions(self):
        packages = Package.objects.bulk_create(
            [Package(**package) for package in valid_package_dataset]
        )
        SubscriptionQueryset.create_subscriptions_for_user(
            self.user1, [package.id for package in packages]
        )
