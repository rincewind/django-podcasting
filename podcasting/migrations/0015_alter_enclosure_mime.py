# Generated by Django 5.0.1 on 2024-02-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasting", "0014_remove_show_owner_alter_show_owner_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enclosure",
            name="mime",
            field=models.CharField(
                choices=[
                    ("aiff", "audio/aiff"),
                    ("mp3", "audio/mpeg"),
                    ("mp4", "audio/mp4"),
                    ("ogg", "audio/ogg"),
                    ("opus", "audio/opus"),
                    ("flac", "audio/flac"),
                    ("wav", "audio/wav"),
                ],
                help_text="Supports mime types of: aiff, mp3, mp4, ogg, opus, flac, wav",
                max_length=4,
                verbose_name="mime format",
            ),
        ),
    ]