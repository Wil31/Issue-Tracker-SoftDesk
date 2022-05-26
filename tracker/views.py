from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tracker.models import Project
from tracker.serializers import ProjectSerializer, ProjectDetailSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return Project.objects.filter(author=current_user)


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
