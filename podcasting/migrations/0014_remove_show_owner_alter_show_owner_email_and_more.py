# Generated by Django 5.0.1 on 2024-02-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasting", "0013_auto_20240206_1729"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="show",
            name="owner",
        ),
        migrations.AlterField(
            model_name="show",
            name="owner_email",
            field=models.EmailField(
                help_text="Email address of the podcast owner (itunes:owner).",
                max_length=254,
                verbose_name="owner email",
            ),
        ),
        migrations.AlterField(
            model_name="show",
            name="owner_name",
            field=models.CharField(
                help_text="Name of the organization, company or Web site owning the podcast. (itunes:owner)",
                max_length=255,
                verbose_name="owner name",
            ),
        ),
    ]
