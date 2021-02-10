import os
from django.core.exceptions import ValidationError
from django.conf import settings


def validate_image_extension(image):
    ext = os.path.splitext(image.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            f'Unsupported file extension. '
            f'Allowed extensions {valid_extensions}'
        )


def validate_size_limit(image):
    file_size = image.size
    limit = settings.MAX_UPLOAD_SIZE
    if file_size > limit:
        raise ValidationError(f'Max size of file is {limit} MB')
