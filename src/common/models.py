import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


def generate_uuid_for_file_with_dir(original_file_name: str, upload_dir: str):
    """
    generates a uuid name for given file and concats it to given dir
    Example: <upload_dir>/193f511b-6061-4b03-b136-2d5fa1b3b39b<.extension>
    """
    extension = original_file_name.split(".")[-1]
    file_name = f"{uuid.uuid4()}.{extension}"
    return os.path.join(upload_dir, file_name)


class BaseModel(models.Model):
    """
    base model for all other models
    """

    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def full_clean_and_save(
        self,
        exclude=None,
        validate_unique=True,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean(exclude, validate_unique)
        self.save(force_insert, force_update, using, update_fields)


class User(AbstractUser):
    """
    user model explicitly implemented for future enhancements
    """


class Access(models.Model):
    """
    This model is used to create content type for generic permissions
    """
