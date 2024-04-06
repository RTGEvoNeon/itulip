from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Проверка на безопасные методы (head, get, options)
        if request.METHOD in permissions.SAFE_METHODS:
            return True 
        return bool(request.user and request.user.is_staff)
