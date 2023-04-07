from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as gt_l

from common.services import BaseService
from common.utils import remove_field_file
from mainapp.models.customer import Customer
from mainapp.serializers.customers import (
    CustomerCreateSerializer,
    CustomerUploadAvatarSerializer,
)


class CustomerService(BaseService):
    """Customer service"""

    def list(self) -> QuerySet:
        """returns a list of customers"""
        return Customer.objects.all()

    def create(self, serializer: CustomerCreateSerializer) -> Customer:
        """create a new customer it doesn't need to handle avatar"""
        return Customer.objects.create(**serializer.validated_data)

    def upload_avatar(self, serializer: CustomerUploadAvatarSerializer) -> Customer:
        """upload avatar for a customer via id and deletes previous file if existed"""
        try:
            customer = Customer.objects.get(id=serializer.validated_data["customer_id"])
        except Customer.DoesNotExist:
            raise ValueError(gt_l("Customer does not exist"))

        customer.current_avatar = customer.avatar
        customer.avatar = serializer.validated_data["avatar"]
        customer.full_clean_and_save()
        remove_field_file(customer.current_avatar)

        return customer
