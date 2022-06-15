from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tracker.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    project_contributor = serializers.StringRelatedField(many=True)
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author",
            "project_contributor",
            "issue_project",
        ]
        read_only_fields = ("author",)

    def create(self, validated_data):
        author = self.context.get("request", None).user

        project = Project.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author=author,
        )
        project.save()

        return project


class ContributorSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta(object):
        model = Contributor
        fields = [
            "id",
            "user",
            "project",
        ]
        read_only_fields = ["project"]

    def create(self, validated_data):
        User = get_user_model()
        user = self.context["request"].user

        project = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])
        contributor_username = self.context["request"].POST.get("user", "[]")
        contributor_user = User.objects.get(username=contributor_username)

        if user == contributor_user:
            raise serializers.ValidationError(
                "The project author cannot be contributor"
            )

        contributor = Contributor.objects.create(user=contributor_user, project=project)
        contributor.save()
        return contributor


class IssueSerializer(serializers.ModelSerializer):
    comment_issue = serializers.StringRelatedField(many=True)
    author = serializers.ReadOnlyField(source="author.username")
    assignee = serializers.ReadOnlyField(source="assignee.username")

    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "project",
            "status",
            "author",
            "assignee",
            "created_time",
            "comment_issue",
        ]
        read_only_fields = ["author", "project", "created_time"]

    def validate(self, data):
        """Check if assignee is a project contributor"""
        User = get_user_model()
        project = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])
        assignee_username = self.context["request"].POST.get("assignee", "[]")
        if assignee_username != "":
            assignee = get_object_or_404(User, username=assignee_username)
            print(assignee)
            print(project.author)

            if assignee == project.author:
                return super().validate(data)
            elif not Contributor.objects.filter(
                user=assignee, project=project
            ).exists():
                error_message = (
                    f"The assignee {str(assignee)} is not a contributor"
                    f" for the project "
                )
                raise serializers.ValidationError(error_message)
        return super().validate(data)

    def create(self, validated_data):
        User = get_user_model()

        author = self.context.get("request", None).user
        project = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])

        assignee_username = self.context["request"].POST.get("assignee", "[]")

        if assignee_username != "":
            assignee = get_object_or_404(User, username=assignee_username)
        else:
            assignee = author

        issue = Issue.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            tag=validated_data["tag"],
            priority=validated_data["priority"],
            project=project,
            status=validated_data["status"],
            author=author,
            assignee=assignee,
        )
        issue.save()
        return issue

    def update(self, instance, validated_data):
        User = get_user_model()

        author = self.context.get("request", None).user

        assignee_username = self.context["request"].POST.get("assignee", "[]")

        if assignee_username != "":
            instance.assignee = User.objects.get(username=assignee_username)
        else:
            instance.assignee = author

        instance.title = validated_data["title"]
        instance.description = validated_data["description"]
        instance.tag = validated_data["tag"]
        instance.priority = validated_data["priority"]
        instance.status = validated_data["status"]
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "description", "author", "issue", "created_time"]
        read_only_fields = ["author", "issue", "created_time"]

    def create(self, validated_data):
        author = self.context.get("request", None).user
        issue_id = self.context.get("view").kwargs["issues_pk"]
        issue = get_object_or_404(Issue, pk=issue_id)

        comment = Comment.objects.create(
            description=validated_data["description"],
            author=author,
            issue=issue,
        )
        comment.save()
        return comment
