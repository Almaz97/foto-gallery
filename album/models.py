from io import BytesIO

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.core.files.base import ContentFile

from album.validators import validate_image_extension, validate_size_limit


class Album(models.Model):
    class Meta:
        db_table = 'album'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='albums'
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/',
        validators=[validate_image_extension, validate_size_limit]
    )
    thumbnail_image = models.ImageField(
        upload_to='thumbnails/', null=True, blank=True
    )
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            image_file = BytesIO()
            img.save(image_file, img.format)
            self.thumbnail_image.save(
                self.image.name, ContentFile(image_file.getvalue()), save=False
            )
            image_file.close()
