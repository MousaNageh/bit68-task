from rest_framework import serializers
from .package_serializer import PackageSerializer
from package.validators.create_packages_validators import CreatePackagesValidator


class CreateSubscriptionSerializer(serializers.Serializer):
    packages = serializers.ListSerializer(
        child=serializers.IntegerField(), allow_empty=False
    )

    def validate(self, attrs):
        attrs["packages"] = CreatePackagesValidator(
            packages_ids=attrs.get("packages"), user=self.context.get("user")
        ).validated_packages_ids
        return attrs


class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    package = PackageSerializer()
