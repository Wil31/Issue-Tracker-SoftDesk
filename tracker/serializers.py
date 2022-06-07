from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tracker.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    project_contributor = serializers.StringRelatedField(many=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'author',
                  'project_contributor',
                  'issue_project',
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
    user = serializers.ReadOnlyField(source='user.username')

    class Meta(object):
        model = Contributor
        fields = ['id',
                  'user',
                  'project',
                  ]

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


class IssueSerializer(serializers.ModelSerializer):
    comment_issue = serializers.StringRelatedField(many=True)
    author = serializers.ReadOnlyField(source='author.username')
    assignee = serializers.ReadOnlyField(source='assignee.username')

    class Meta:
        model = Issue
        fields = ['id',
                  'title',
                  'description',
                  'tag',
                  'priority',
                  'project',
                  'status',
                  'author',
                  'assignee',
                  'created_time',
                  'comment_issue'
                  ]
        read_only_fields = ['author', 'project', 'created_time']

    def create(self, validated_data):
        author = self.context.get("request", None).user

        project = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])

        issue = Issue.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            tag=validated_data["tag"],
            priority=validated_data["priority"],
            project=project,
            status=validated_data["status"],
            author=author,
            assignee=author,
        )
        issue.save()
        return issue


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id',
                  'description',
                  'author',
                  'issue',
                  'created_time'
                  ]
        read_only_fields = ['author', 'issue', 'created_time']

    # def create(self, validated_data):
    #     author = self.context.get("request", None).user
    #
    #     issue = Issue.object.get(pk=self.context.get("view").kwargs["issue_pk"])
    #
    #     comment = Comment.objects.create(
    #         description=validated_data["description"],
    #         author=author,
    #         issue=issue,
    #     )
    #     comment.save()
    #     return comment
