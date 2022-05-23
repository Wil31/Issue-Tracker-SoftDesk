from rest_framework.viewsets import ReadOnlyModelViewSet

from tracker.models import Project
from tracker.serializers import ProjectSerializer, ProjectDetailSerializer


class ProjectViewset(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
