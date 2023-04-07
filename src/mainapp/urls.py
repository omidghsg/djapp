from django.urls import path

from mainapp.views.customers import CustomerCreate, CustomerList, CustomerUploadAvatar
from mainapp.views.token import CreateToken

app_name = "mainapp"

urlpatterns = [
    path("token/", CreateToken.as_view(), name="token"),
    path("customers/", CustomerList.as_view(), name="customers"),
    path("customers/create/", CustomerCreate.as_view(), name="customers-create"),
    path(
        "customers/upload-avatar/",
        CustomerUploadAvatar.as_view(),
        name="customers-upload-avatar",
    ),
]
