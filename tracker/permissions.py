from django.shortcuts import get_object_or_404
from rest_framework import permissions

from tracker.models import Project, Contributor


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


class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    message = "Only the Comment author can do this action"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsProjectContributor(permissions.BasePermission):
    message = "Only Project contributors or authors can do this action"

    def has_permission(self, request, view):
        project = get_object_or_404(Project, pk=view.kwargs["project_pk"])
        user = request.user

        if (
            user == project.author
            or Contributor.objects.filter(user=user, project=project).exists()
        ):
            return True
