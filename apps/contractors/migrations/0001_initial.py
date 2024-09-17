# Generated by Django 5.1.1 on 2024-09-17 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("agencies", "0002_agency_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contractor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("second_name", models.CharField(max_length=255)),
                (
                    "agency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="contractors", to="agencies.agency"
                    ),
                ),
            ],
        ),
    ]
