from django.db import models
from django.utils.translation import gettext as _


class Character(models.Model):
    player = models.ForeignKey(
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
    sub_class = models.CharField(_("Subclass"), max_length=256, null=True, blank=True)

    profile_image = models.ImageField(
        _("Profile image"), help_text=_("Main display image")
    )

    @property
    def full_name(self):
        name_parts = [
            part
            for part in [self.first_name, self.middle_names, self.infix, self.last_name]
            if part
        ]
        return " ".join(name_parts)

    @property
    def race_class_description(self):
        return (
            f"The {self.race} {self.character_class} - {self.sub_class or ''}"
            if self.sub_class
            else f"The {self.race or ''} {self.character_class}"
        )

    def __str__(self):
        return self.full_name
