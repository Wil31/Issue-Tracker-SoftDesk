from django.contrib import admin

from tracker.models import Project, Contributor, Issue, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "type", "author")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "assignee")


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment)
