# Generated by Django 5.0.3 on 2024-04-26 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilder', '0005_alter_bild_image_url_alter_bild_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bild',
            name='description',
        ),
    ]