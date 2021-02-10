from django.db import models
from django.contrib.auth.models import User

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
    _thumbnail_image = models.ImageField(
        upload_to='thumbnails/', null=True, blank=True
    )
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
