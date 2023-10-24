from django.contrib import admin
from package.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user", "package"]
    list_select_related = ["user", "package"]
    list_filter = ["package"]
    search_fields = ["package__name", "user__email", "user__full_name"]
