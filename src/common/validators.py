import os
from typing import List

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as gt_l


@deconstructible
class FileSizeValidator:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size

    def __call__(self, value: str) -> None:
        if value.size > self.max_size:
            raise ValidationError(gt_l("The maximum file size has been exceeded."))
        else:
            return value

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, FileSizeValidator) and self.max_size == __o.max_size


@deconstructible
class FileExtensionValidator:
    def __init__(self, valid_extensions: List[str]):
        self.valid_extensions = valid_extensions

    def __call__(self, value: str) -> None:
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        if not ext.lower() in self.valid_extensions:
            raise ValidationError(gt_l("Unsupported file extension."))
        else:
            return value

    def __eq__(self, __o: object) -> bool:
        return (
            isinstance(__o, FileExtensionValidator)
            and self.valid_extensions == __o.valid_extensions
        )
