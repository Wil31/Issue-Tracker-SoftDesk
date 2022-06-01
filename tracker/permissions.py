from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = "Only the Project author can do this action"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsIssueAuthorOrReadOnly(permissions.BasePermission):
    message = "Only the Issue author can do this action"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
