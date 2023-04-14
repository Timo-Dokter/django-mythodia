# Generated by Django 4.1.7 on 2023-04-14 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=256, verbose_name="First name"),
                ),
                (
                    "infix",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="Infix"
                    ),
                ),
                (
                    "middle_names",
                    models.CharField(
                        blank=True,
                        max_length=256,
                        null=True,
                        verbose_name="Middle names",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="Last name"
                    ),
                ),
                ("race", models.CharField(max_length=256, verbose_name="Race")),
                (
                    "character_class",
                    models.CharField(max_length=256, verbose_name="Class"),
                ),
                (
                    "sub_class",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="Subclass"
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        help_text="Main display image",
                        upload_to="",
                        verbose_name="Profile image",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("first_name", "infix")},
            },
        ),
    ]
