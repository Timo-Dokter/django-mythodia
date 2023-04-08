from django.db import models
from django.utils.translation import gettext as _


class Character(models.Model):
    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    first_name = models.CharField(_("First name"), max_length=256)
    infix = models.CharField(_("Infix"), max_length=256, null=True, blank=True)
    middle_names = models.CharField(
        _("Middle names"), max_length=256, null=True, blank=True
    )
    last_name = models.CharField(_("Last name"), max_length=256, null=True, blank=True)

    race = models.CharField(_("Race"), max_length=256)
    character_class = models.CharField(_("Class"), max_length=256)
    sub_class = models.CharField(_("Subclass"), max_length=256)

    @property
    def full_name(self):
        if self.middle_names:
            return (
                f"{self.first_name} {self.middle_names} {self.infix} {self.last_name}"
            )
        return f"{self.first_name} {self.infix} {self.last_name}"

    @property
    def race_class_description(self):
        return f"{self.full_name},"

    class Meta:
        unique_together = ["first_name", "infix"]
