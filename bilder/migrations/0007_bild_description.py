# Generated by Django 5.0.3 on 2024-04-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilder', '0006_remove_bild_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bild',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]