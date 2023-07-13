from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from ..managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("Email address"),
        unique=True,
        error_messages={"unique": _("A user with that email address already exists.")},
    )
    first_name = models.CharField(_("First name"), max_length=256, blank=True)
    last_name = models.CharField(_("Last name"), max_length=256, blank=True)

    is_staff = models.BooleanField(
        _("Admin status"),
        default=False,
        help_text=_("Designates wheter the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    is_dm = models.BooleanField(
        _("Dungeon Master"),
        default=False,
        help_text=_("Designates whether this user is a Dungeon Master."),
    )

    date_joined = models.DateTimeField(_("Date joined"), default=timezone.now)

    objects = AccountManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def __str__(self):
        return self.full_name

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
