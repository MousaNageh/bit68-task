from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from package.serializers.subscription_serializer import (
    CreateSubscriptionSerializer,
    SubscriptionSerializer,
)
from package.queryset.subscription_queryset import SubscriptionQueryset
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]
    paginator = PageNumberPagination()

    def get(self, request):
        query = SubscriptionQueryset.get_user_subscriptions(
            user=request.user, select_packages=True
        )
        paginated_queryset = self.paginator.paginate_queryset(query, request)
        serializer = SubscriptionSerializer(paginated_queryset, many=True)
        return self.paginator.get_paginated_response(serializer.data)

    @staticmethod
    def post(request):
        user = request.user
        serializer = CreateSubscriptionSerializer(
            data=request.data, context={"user": user}
        )
        serializer.is_valid(raise_exception=True)
        SubscriptionQueryset.create_subscriptions_for_user(
            user=user, packages_ids=serializer.validated_data.get("packages")
        )
        return Response(
            {"created": "packages has been created"}, status=HTTP_201_CREATED
        )
