from django.conf import settings
from django.db import models


class Project(models.Model):
    TYPE_CHOICES = (
        ("BE", "Back-end"),
        ("FE", "Front-end"),
        ("IOS", "IOS"),
        ("ANDROID", "Android"),
    )
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_contributor",
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="project_contributor"
    )

    class Meta:
        unique_together = ("user", "project")

    def __str__(self):
        return f"{self.user}"


class Issue(models.Model):
    PRIORITY = [
        ("LO", "Low"),
        ("ME", "Medium"),
        ("HI", "High"),
    ]

    TAG = [("BUG", "Bug"), ("IMPR", "Improvement"), ("TASK", "Task")]

    STATUT = [("TODO", "To do"), ("IN_PRO", "In progress"), ("DONE", "Done")]
    title = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(max_length=500, blank=True)
    tag = models.CharField(max_length=4, choices=TAG)
    priority = models.CharField(max_length=2, choices=PRIORITY)
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="issue_project"
    )
    status = models.CharField(max_length=6, choices=STATUT)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="issue_author",
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="issue_assignee",
        default=author,
    )
    created_time = models.DateTimeField(verbose_name="created time", auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField(max_length=500, unique=True, blank=False)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="user_comment",
    )
    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, related_name="comment_issue"
    )
    created_time = models.DateTimeField(verbose_name="created time", auto_now_add=True)

    def __str__(self):
        return self.description
