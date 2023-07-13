from import_export import resources

from ..models import Encounter


class EncounterResource(resources.ModelResource):
    class Meta:
        model = Encounter
        fields = ("name", "description", "regions")
        export_order = ("name", "description", "regions")
