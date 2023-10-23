from django.urls import path
from package.views.package_views import PackageView

urlpatterns = [path("", PackageView.as_view(), name="package-list")]
