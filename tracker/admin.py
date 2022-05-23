from django.contrib import admin

from tracker.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'type', 'author')


admin.site.register(Project, ProjectAdmin)
