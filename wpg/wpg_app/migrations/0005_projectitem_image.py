# Generated by Django 5.0.2 on 2024-07-15 10:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpg_app', '0004_remove_projectitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectitem',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, height_field='image_height', max_length=255, upload_to='images/%Y/%m/%d/', width_field='image_width'),
            preserve_default=False,
        ),
    ]
