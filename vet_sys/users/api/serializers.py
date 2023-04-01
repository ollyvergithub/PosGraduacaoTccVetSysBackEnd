from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    permissoes = serializers.SerializerMethodField('get_user_permissions')

    def get_user_permissions(self, user):
        perms = []
        for group in user.groups.all():
            for permission in group.permissions.all():
                perms.append(permission.codename)

        return perms

    class Meta:
        model = User
        # fields = '__all__'
        fields = ["id", "is_superuser", "username", "email", "is_staff", "is_active", "name", "permissoes"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }
