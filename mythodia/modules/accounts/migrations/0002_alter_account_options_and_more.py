# Generated by Django 4.1.7 on 2023-04-06 14:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="account",
            options={"verbose_name": "Account", "verbose_name_plural": "Accounts"},
        ),
        migrations.RenameField(
            model_name="account",
            old_name="is_staff",
            new_name="is_admin",
        ),
    ]