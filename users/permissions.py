from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Object-level permission to only allow user of an object(book) to view it.
    """

    def has_object_permission(self, request, view, obj):
        print(request.user)
        print(view)
        print(obj)

        if obj == request.user:
            return True
        return False
