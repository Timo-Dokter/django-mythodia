from import_export import resources

from ..models import Scenery


class SceneryResource(resources.ModelResource):
    class Meta:
        model = Scenery
        fields = ("name", "description", "regions")
        export_order = ("name", "description", "regions")
