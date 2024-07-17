# Generated by Django 5.0.2 on 2024-07-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpg_app', '0007_alter_projectitem_projectimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectItem',
        ),
    ]
