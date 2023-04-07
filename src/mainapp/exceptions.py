from django.utils.translation import gettext_lazy as gt_l

from common.exceptions import ApplicationError


class CustomerNotFound(ApplicationError):
    """Customer not found"""

    message = gt_l("Customer not found")
    status = 404
