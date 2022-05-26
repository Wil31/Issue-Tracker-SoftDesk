from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tracker.models import Project, Contributor
from tracker.serializers import ProjectSerializer, ContributorSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return Project.objects.filter(author=current_user)


class ContributorViewSet(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = []

    def get_queryset(self):
        return Contributor.objects.all()
