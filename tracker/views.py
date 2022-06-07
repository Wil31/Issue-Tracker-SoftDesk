from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tracker.models import Project, Contributor, Comment
from tracker.permissions import IsAuthorOrReadOnly, IsIssueAuthorOrReadOnly, \
    IsCommentAuthorOrReadOnly
from tracker.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, \
    CommentSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        current_user = self.request.user
        contributors = Contributor.objects.filter(user=self.request.user)
        return (Project.objects.filter(author=current_user) |
                Project.objects.filter(project_contributor__in=contributors)) \
            # .distinct()


class ContributorViewSet(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = []

    def get_queryset(self):
        return Contributor.objects.all()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsIssueAuthorOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        project = (Project.objects.filter(pk=project_id,
                                          project_contributor__user=self.request.user)
                   | Project.objects.filter(pk=project_id, author=self.request.user))
        return project[0].issue_project.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()
