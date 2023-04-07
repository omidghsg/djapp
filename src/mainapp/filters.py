from django_filters import FilterSet

from mainapp.models.customer import Customer


class CustomerFilter(FilterSet):
    class Meta:
        model = Customer
        fields = {
            "name": ["exact", "contains"],
            "email": ["exact"],
        }
