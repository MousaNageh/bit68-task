from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from package.serializers.package_serializer import (
    PackageSerializer,
    PackageQueryParamSerializer,
)
from rest_framework.pagination import PageNumberPagination
from package.queryset.package_queryset import PackageQueryset


class PackageView(ListAPIView):
    serializer_class = PackageSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        serializer = PackageQueryParamSerializer(data=self.request.GET)
        serializer.is_valid(raise_exception=True)
        return PackageQueryset.all_package(
            ordering=serializer.validated_data.get("ordering"),
            keyword=serializer.validated_data.get("keyword"),
        )
