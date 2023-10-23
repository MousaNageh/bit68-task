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
