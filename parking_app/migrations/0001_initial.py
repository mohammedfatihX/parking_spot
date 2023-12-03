# Generated by Django 4.2.7 on 2023-12-03 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="ParkingPlace",
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
                ("name", models.CharField(max_length=10, unique=True)),
                ("is_available", models.BooleanField(default=True)),
                ("date_reserved", models.DateTimeField(blank=True, null=True)),
                (
                    "reserved_by_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="parking_app.user",
                    ),
                ),
            ],
        ),
    ]