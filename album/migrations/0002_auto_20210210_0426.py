# Generated by Django 3.1.6 on 2021-02-10 04:26

import album.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(upload_to='images/', validators=[album.validators.validate_image_extension, album.validators.validate_size_limit]),
        ),
    ]
