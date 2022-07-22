from django.contrib import admin

from .models import About, Project, TechnologyUsed, Subject, Picture


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(TechnologyUsed)
class TechnologyUsedAdmin(admin.ModelAdmin):
    pass


@admin.register(Picture)
class Picture(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(Subject)
class Subject(admin.ModelAdmin):
    pass
