# Generated by Django 5.0.1 on 2024-01-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasting", "0006_episode_tags_show_category_show_tags_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="episode",
            name="number",
            field=models.IntegerField(default=0, verbose_name="Episode-Number"),
            preserve_default=False,
        ),
    ]