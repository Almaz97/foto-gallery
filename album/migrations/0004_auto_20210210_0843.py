# Generated by Django 3.1.6 on 2021-02-10 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20210210_0537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='_thumbnail_image',
            new_name='thumbnail_image',
        ),
    ]
