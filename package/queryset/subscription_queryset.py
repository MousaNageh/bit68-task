from package.models import Subscription


class SubscriptionQueryset:
    @staticmethod
    def get_user_subscriptions(user, filter_package_ids=None, select_packages=False):
        query = Subscription.objects.filter(user=user)
        if filter_package_ids:
            query = query.filter(package_id__in=filter_package_ids)
        if select_packages:
            query = query.select_related("package")
        return query

    @staticmethod
    def create_subscriptions_for_user(user, packages_ids: list):
        subscriptions = [
            Subscription(user=user, package_id=packages_id)
            for packages_id in packages_ids
        ]
        Subscription.objects.bulk_create(subscriptions, batch_size=400)
