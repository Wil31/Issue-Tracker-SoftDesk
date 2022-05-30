from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tracker.models import Project, Contributor


class ProjectSerializer(ModelSerializer):
    project_contributor = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'author',
                  'project_contributor'
                  ]
        read_only_fields = ("author",)

    def create(self, validated_data):
        author = self.context.get("request", None).user  # get the access token

        project = Project.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author=author
        )
        project.save()

        return project


class ContributorSerializer(ModelSerializer):
    class Meta(object):
        model = Contributor
        fields = ('id',
                  'user',
                  'project',
                  )

    def validate_user(self, value):
        user = self.context['request'].user
        if user == value:
            raise serializers.ValidationError(
                "The project author cannot be contributor")
        return value

    def create(self, validated_data):
        project = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])

        contributor = Contributor.objects.create(
            user=validated_data["user"],
            project=project
        )
        contributor.save()
        return contributor
