from inject import Binder

from mainapp.services.customer import CustomerService

__all__ = ["di_config"]


def di_config(binder: Binder) -> None:
    binder.bind(CustomerService, CustomerService())
