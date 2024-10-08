# Generated by Django 5.0.6 on 2024-07-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Web", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scriptexecution",
            name="status",
            field=models.CharField(
                choices=[
                    ("success", "Success"),
                    ("failed", "Failed"),
                    ("stop", "Stop"),
                ],
                default="failed",
                max_length=20,
            ),
        ),
    ]
