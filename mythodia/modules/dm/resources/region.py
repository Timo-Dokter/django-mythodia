from import_export import resources

from ..models import Region


class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
        fields = ("name",)
        export_order = ("name",)
