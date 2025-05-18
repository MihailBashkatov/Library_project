from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow user of an object(habit) to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if obj.habit_user == request.user:
            return True
        return False


class IsOwnerNiceHabit(permissions.BasePermission):
    """
    Object-level permission to only allow user of an object(habit) to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if obj.nice_habit_user == request.user:
            return True
        return False
