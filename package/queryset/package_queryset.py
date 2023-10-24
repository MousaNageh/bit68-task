from package.models import Package


class PackageQueryset:
    @staticmethod
    def all_package(keyword=None, ordering=None):
        query = Package.objects.all()
        if keyword:
            query = query.filter(name__icontains=keyword)
        if ordering:
            query = query.order_by(ordering)
        return query

    @staticmethod
    def get_packages_by_id(package_ids: list, ids_only=False):
        query = Package.objects.filter(id__in=package_ids)
        if ids_only:
            query = list(query.values_list("id", flat=True))
        return query
