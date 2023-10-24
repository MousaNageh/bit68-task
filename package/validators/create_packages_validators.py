from package.queryset.package_queryset import PackageQueryset
from rest_framework.exceptions import ValidationError

from package.queryset.subscription_queryset import SubscriptionQueryset


class CreatePackagesValidator:
    def __init__(self, packages_ids: list, user):
        self._packages_ids = self._get_unique_packages_ids(packages_ids)
        self._user = user

    @property
    def validated_packages_ids(self):
        self._validate_packages_ids_exist()
        self._validate_if_user_has_packages_created_before()
        return self._packages_ids

    def _validate_packages_ids_exist(self):
        existing_packages_ids = PackageQueryset.get_packages_by_id(
            self._packages_ids, ids_only=True
        )
        if len(existing_packages_ids) != len(self._packages_ids):
            not_exists_packages_ids = [
                package_id
                for package_id in self._packages_ids
                if package_id not in existing_packages_ids
            ]
            if not_exists_packages_ids:
                raise ValidationError(
                    f"packages with ids {not_exists_packages_ids} not exists ."
                )

    def _validate_if_user_has_packages_created_before(self):
        user_packages = SubscriptionQueryset.get_user_subscriptions(
            user=self._user, filter_package_ids=self._packages_ids
        )
        existing_packages = [package.id for package in user_packages]
        if existing_packages:
            raise ValidationError(
                f"packages with ids {existing_packages} is already created ."
            )

    @staticmethod
    def _get_unique_packages_ids(packages_ids):
        return list(set(packages_ids))
