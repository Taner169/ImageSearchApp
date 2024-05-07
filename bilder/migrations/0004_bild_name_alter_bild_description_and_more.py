# Generated by Django 5.0.3 on 2024-04-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilder', '0003_remove_bild_name_alter_bild_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bild',
            name='name',
            field=models.CharField(default='Default Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='bild',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bild',
            name='image_url',
            field=models.URLField(),
        ),
    ]