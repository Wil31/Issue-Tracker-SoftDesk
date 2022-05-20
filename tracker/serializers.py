from rest_framework.serializers import ModelSerializer

from tracker.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'type']
