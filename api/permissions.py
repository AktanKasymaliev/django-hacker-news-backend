from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return bool(request.user == obj.author_name)
        except Exception as e:
            return bool(request.user == obj.author)