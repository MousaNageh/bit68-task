from django.urls import path
from package.views.package_views import PackageView
from package.views.subscription_view import SubscriptionView

urlpatterns = [
    path("", PackageView.as_view(), name="package-list"),
    path("subscription", SubscriptionView.as_view(), name="subscription-api"),
]
