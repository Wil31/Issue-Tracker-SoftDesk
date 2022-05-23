from django.conf import settings
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    BACKEND = 'BACKEND'
    FRONTEND = 'FRONTEND'
    IOS = 'IOS'
    ANDROID = 'ANDROID'

    TYPE_CHOICES = (
        (BACKEND, 'Back-end'),
        (FRONTEND, 'Front-end'),
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    )

    type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='Type')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="user"
                             )
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name="project"
                                )
    PERMISSION_CHOICES = ()
    permission = models.CharField(max_length=30,
                                  choices=PERMISSION_CHOICES,
                                  verbose_name='Permission'
                                  )

    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = 'CONTRIBUTOR'
    ROLE_CHOICES = (
        (AUTHOR, 'Author'),
        (CONTRIBUTOR, 'Contributor')
    )
    role = models.CharField(max_length=30,
                            choices=ROLE_CHOICES,
                            verbose_name='Role'
                            )

    class Meta:
        unique_together = ("user", "project")
