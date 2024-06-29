from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка прав доступа для владельца модуля."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()
