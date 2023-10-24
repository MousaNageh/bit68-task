from django.contrib import admin
from package.models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name"]
