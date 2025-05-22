from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow user of an object(book) to view it.
    """

    def has_object_permission(self, request, view, obj):

        if obj.client == request.user:
            return True
        return False


class IsLibrarian(permissions.BasePermission):
    """
    Request permission to only allow librarian to modify book
    """

    def has_permission(self, request, view):

        if request.user.is_librarian:
            return True
        return False
