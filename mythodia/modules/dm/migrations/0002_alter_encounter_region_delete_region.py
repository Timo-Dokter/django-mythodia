# Generated by Django 4.1.7 on 2023-07-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dm", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="encounter",
            name="region",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Arctic"),
                    (2, "Coastal"),
                    (3, "Desert"),
                    (4, "Forest"),
                    (5, "Grassland"),
                    (6, "Hill"),
                    (7, "Mountain"),
                    (8, "Swamp"),
                    (9, "Underdark"),
                    (10, "Underwater"),
                ],
                null=True,
            ),
        ),
        migrations.DeleteModel(
            name="Region",
        ),
    ]
