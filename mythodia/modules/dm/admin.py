from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *
from .resources import *


@admin.register(Encounter)
class EncounterAdmin(ImportExportModelAdmin):
    list_filter = ("regions",)
    list_display = ("name", "list_regions", "description")
    search_fields = ("name", "description", "regions")
    ordering = ("name",)
    resource_class = EncounterResource


@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    resource_class = RegionResource


@admin.register(Scenery)
class SceneryAdmin(ImportExportModelAdmin):
    list_filter = ("regions",)
    list_display = ("name", "list_regions", "description")
    search_fields = ("name", "description", "regions")
    ordering = ("name",)
    resource_class = SceneryResource
