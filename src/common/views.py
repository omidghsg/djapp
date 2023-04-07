from django.utils.translation import gettext_lazy as gt_l
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView


class BaseAPIView(APIView):
    """Base API View for all other API views"""

    def filtered_queryset(self, query_params, queryset=None, raise_exception=False, **kwargs):
        filterset = self.filterset_class(query_params, queryset, **kwargs)
        if raise_exception and not filterset.is_valid():
            raise ValidationError({gt_l("filterset errors"): filterset.errors})
        return filterset.qs
