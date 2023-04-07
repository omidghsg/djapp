from django.contrib import admin

from mainapp.models.customer import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    search_fields = (
        "name",
        "email",
    )
    ordering = ("name",)
