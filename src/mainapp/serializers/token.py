from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as gt_l
from rest_framework import serializers


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )
        if not user:
            msg = gt_l("Unable to authenticate with provided credentials.")
            raise serializers.ValidationError(msg, code="authentication")
        attrs["user"] = user
        return super().validate(attrs)
