# Generated by Django 5.0.1 on 2024-01-27 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasting", "0008_episode_season"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shownote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField(default=0)),
                ("text", models.TextField(blank=True)),
                (
                    "url",
                    models.URLField(
                        help_text="URL of the show note link", verbose_name="url"
                    ),
                ),
                (
                    "episode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="podcasting.episode",
                        verbose_name="episode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Shownote",
                "verbose_name_plural": "Shownotes",
                "ordering": ("episode", "position"),
                "unique_together": {("episode", "url")},
            },
        ),
    ]