# Generated by Django 5.0.1 on 2024-01-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasting", "0007_episode_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="episode",
            name="season",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="Season-Number"
            ),
        ),
    ]