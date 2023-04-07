from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as gt_l

from common.models import BaseModel, generate_uuid_for_file_with_dir
from common.validators import FileExtensionValidator, FileSizeValidator


def generate_uuid_for_author_avatar(_, original_file_name: str):
    return generate_uuid_for_file_with_dir(
        original_file_name,
        settings.UPLOAD_TO_CUSTOMER_AVATAR,
    )


class Customer(BaseModel):
    """
    Customer model
    """

    name = models.CharField(gt_l("Name"), max_length=200, blank=False, null=False)
    email = models.EmailField(gt_l("Email"), blank=False, null=False, unique=True)
    avatar = models.ImageField(
        gt_l("Avatar"),
        upload_to=generate_uuid_for_author_avatar,
        blank=True,
        null=True,
        validators=[
            FileSizeValidator(settings.CUSTOMER_AVATAR_MAX_SIZE),
            FileExtensionValidator(settings.CUSTOMER_AVATAR_ALLOWED_EX),
        ],
    )

    def __str__(self):
        return f"{self.name} - {self.email}"
