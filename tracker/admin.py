from django.contrib import admin

from tracker.models import Project, Contributor, Issue


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'type', 'author')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor)
admin.site.register(Issue)
