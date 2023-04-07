from rest_framework import serializers

from mainapp.models.customer import Customer


class CustomerListSerializer(serializers.ModelSerializer):
    """customer list serializer"""

    class Meta:
        model = Customer
        fields = "__all__"


class CustomerCreateSerializer(serializers.ModelSerializer):
    """customer create serializer it doesn't need to handle avatar"""

    class Meta:
        model = Customer
        fields = ("name", "email")


class CustomerUploadAvatarSerializer(serializers.ModelSerializer):
    """customer upload avatar serializer"""

    customer_id = serializers.IntegerField(required=True, allow_null=False)
    avatar = serializers.ImageField(required=True, allow_null=False)

    class Meta:
        model = Customer
        fields = ("customer_id", "avatar")
