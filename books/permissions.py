from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow user of an object(book) to view it.
    """

    def has_object_permission(self, request, view, obj):

        if obj.client == request.user:
            return True
        return False


#
#
# class IsOwnerNiceHabit(permissions.BasePermission):
#     """
#     Object-level permission to only allow user of an object(habit) to edit it.
#     """
#
#     def has_object_permission(self, request, view, obj):
#
#         if obj.nice_habit_user == request.user:
#             return True
#         return False


class IsLibrarian(permissions.BasePermission):
    """
    Object-level permission to only allow librarian of an object(book) to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.user.is_librarian:
            return True
        return False


class IsLibrarianAddBook(permissions.BasePermission):
    """
    Request permission to only allow librarian to add book
    """

    def has_permission(self, request, view):

        if request.user.is_librarian:
            return True
        return False
