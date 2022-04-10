from django.contrib import admin

from portfolio.models import About, Project, TechnologyUsed


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(TechnologyUsed)
class TechnologyUsedAdmin(admin.ModelAdmin):
    pass
