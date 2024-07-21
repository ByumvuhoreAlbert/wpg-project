# Generated by Django 5.0.2 on 2024-07-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpg_app', '0013_image_delete_project_delete_project_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
