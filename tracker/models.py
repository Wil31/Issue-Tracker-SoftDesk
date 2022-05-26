from django.conf import settings
from django.db import models


class Project(models.Model):
    TYPE_CHOICES = (
        ('BE', 'Back-end'),
        ('FE', 'Front-end'),
        ('IOS', 'IOS'),
        ('ANDROID', 'Android'),
    )
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.RESTRICT)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="user_contributor"
                             )
    project = models.ForeignKey(to=Project,
                                on_delete=models.CASCADE,
                                related_name="project_contributor"
                                )

    class Meta:
        unique_together = ("user", "project")


class Issue(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    project = models.ForeignKey(to=Project,
                                on_delete=models.CASCADE
                                )
    status = models.CharField(max_length=255)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='issue_author'
                               )
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='issue_assignee',
                                 default=None
                                 )
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=True)


class Comment(models.Model):
    description = models.TextField(blank=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE
                               )
    issue = models.ForeignKey(to=Issue,
                              on_delete=models.CASCADE
                              )
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=True)
