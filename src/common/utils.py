from typing import Union

from django.db.models.fields.files import FieldFile, ImageFieldFile


def remove_field_file(instance_field: Union[FieldFile, ImageFieldFile]) -> None:
    """
    checks if there is a file related to given field
    and deletes it from file system
    """
    import os

    if instance_field and os.path.isfile(instance_field.path):
        os.remove(instance_field.path)
