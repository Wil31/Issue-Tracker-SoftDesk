from rest_framework.viewsets import ReadOnlyModelViewSet

from tracker.models import Project
from tracker.serializers import ProjectSerializer


class ProjectViewset(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)
