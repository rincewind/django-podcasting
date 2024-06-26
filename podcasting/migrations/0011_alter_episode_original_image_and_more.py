# Generated by Django 5.0.1 on 2024-02-06 14:52

import podcasting.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasting", "0010_remove_show_category_show_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episode",
            name="original_image",
            field=models.ImageField(
                blank=True,
                help_text='\n                A podcast must have 3000 x 3000 pixel cover art in JPG or PNG\n                format using RGB color space. See our technical spec for\n                details. To be eligible for featuring on iTunes Stores,\n                choose an attractive, original, and square JPEG (.jpg) or\n                PNG (.png) image at a size of 3000x3000 pixels. The image\n                will be scaled down to 50x50 pixels at smallest in iTunes.\n                For reference see the <a\n                href="http://www.apple.com/itunes/podcasts/specs.html#metadata">iTunes\n                Podcast specs</a>.<br /><br /> For episode artwork to\n                display in iTunes, image must be <a\n                href="http://answers.yahoo.com/question/index?qid=20080501164348AAjvBvQ">\n                saved to file\'s <strong>metadata</strong></a> before\n                enclosure uploading!',
                upload_to=podcasting.models.get_episode_upload_folder,
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="show",
            name="original_image",
            field=models.ImageField(
                blank=True,
                help_text='\n                A podcast must have 3000 x 3000 pixel cover art in JPG or PNG\n                format using RGB color space. See our technical spec for\n                details. To be eligible for featuring on iTunes Stores,\n                choose an attractive, original, and square JPEG (.jpg) or\n                PNG (.png) image at a size of 3000 x 3000 pixels. The image\n                will be scaled down to 50x50 pixels at smallest in iTunes.\n                For reference see the <a\n                href="http://www.apple.com/itunes/podcasts/specs.html#metadata">iTunes\n                Podcast specs</a>.<br /><br /> For episode artwork to\n                display in iTunes, image must be <a\n                href="http://answers.yahoo.com/question/index?qid=20080501164348AAjvBvQ">\n                saved to file\'s <strong>metadata</strong></a> before\n                enclosure uploading!',
                upload_to=podcasting.models.get_show_upload_folder,
                verbose_name="image",
            ),
        ),
    ]
