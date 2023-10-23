from rest_framework import serializers


class PackageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.FloatField()


class PackageQueryParamSerializer(serializers.Serializer):
    PRICE_ORDERING = [
        ("price", "price"),
        ("-price", "-price"),
    ]
    ordering = serializers.ChoiceField(
        choices=PRICE_ORDERING, allow_null=True, allow_blank=True, required=False
    )
    keyword = serializers.CharField(allow_null=True, allow_blank=True, required=False)
