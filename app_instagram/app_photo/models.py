from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from pathlib import Path
from uuid import uuid4


def validate_file_size(value):
    file_size = value.size

    if file_size > 1_000_000:
        raise ValidationError("Max file size - 1 mb")
    return value


def upload_image(instance, filename):
    upload_to = Path(instance.user.username) if instance.user else Path('images')
    ext = Path(filename).suffix
    new_filename = f'{uuid4().hex}{ext}'
    return str(upload_to / new_filename)


class Picture(models.Model):
    description = models.CharField(max_length=300)
    path = models.ImageField(upload_to=upload_image, validators=[])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)