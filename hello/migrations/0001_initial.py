# Generated by Django 5.1 on 2024-08-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Greeting",
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
                    "when",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
            ],
        ),
    ]
