from django.contrib import admin

from tracker.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'type')


admin.site.register(Project, ProjectAdmin)
