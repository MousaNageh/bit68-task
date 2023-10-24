from django.contrib.auth import get_user_model
from .package_model import Package
from django.db import models


class Subscription(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name="user_subscriptions",
        on_delete=models.CASCADE,
        db_index=True
    )
    package = models.ForeignKey(
        Package,
        related_name="package_subscriptions",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [("user", "package")]
