from django.db import models


class Encounter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    regions = models.ManyToManyField("dm.Region", blank=True, related_name="encounters")

    @property
    def list_regions(self):
        return ", ".join([region.name for region in self.regions.all()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Encounter"
        verbose_name_plural = "Encounters"
        ordering = ["name"]
