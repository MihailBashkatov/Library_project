from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    message = 'No access'

    def has_object_permission(self, request, view, obj):
        return obj == request.user
