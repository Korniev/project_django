from django.db import models
from django.core.exceptions import ValidationError


def validate_file_size(value):
    file_size = value.size

    if file_size > 1_000_000:
        raise ValidationError("Max file size - 1 mb")
    return value

class Picture(models.Model):
    description = models.CharField(max_length=300)
    path = models.ImageField(upload_to='images', validators=[])
