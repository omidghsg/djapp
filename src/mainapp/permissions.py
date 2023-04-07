from __future__ import annotations

from typing import List, Tuple, TypedDict

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import TextChoices

from common.models import Access


class AppPermissions(TextChoices):
    app_name = "mainapp"

    CUSTOMER_ADMIN = "customer_admin", "Customer Admin"


def get_fullname(permission: AppPermissions) -> str:
    return f"{permission.__class__.app_name}.{permission.value}"


class PermissionsDict(TypedDict):
    """
    TypedDict for permissions
    """

    codename: str
    permission: Permission


def create_permissions(
    app_permissions: List[Tuple[str, str]],
    fake: bool = False,
) -> PermissionsDict:
    """
    Create permissions for the app
    and returns a dict with the permissions created
    """
    permissions_dict = {}
    content_type = ContentType.objects.get_for_model(Access)

    for codename, name in app_permissions:
        if not Permission.objects.filter(
            codename=codename,
            content_type=content_type,
        ).exists():
            if not fake:
                permission = Permission.objects.create(
                    codename=codename,
                    name=name,
                    content_type=content_type,
                )
            permissions_dict[codename] = permission

    return permissions_dict
