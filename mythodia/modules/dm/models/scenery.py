from django.db import models


class Scenery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    regions = models.ManyToManyField("dm.Region", blank=True, related_name="scenery")

    @property
    def list_regions(self):
        return ", ".join([region.name for region in self.regions.all()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Scenery"
        verbose_name_plural = "Scenery"
        ordering = ["name"]
