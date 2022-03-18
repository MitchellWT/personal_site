import markdown
from django.shortcuts import get_object_or_404, render
from django.utils.safestring import mark_safe

from portfolio.models import About, Project


def index(request):
    return render(request, "pages/index.html")


def about(request):
    obj = get_object_or_404(About)
    html_body = markdown.markdown(obj.body)
    return render(request, "pages/about.html", {
        "html_body": mark_safe(html_body),
    })


def blog(request):
    return render(request, "pages/blog.html")


def projects(request):
    projects = list(Project.objects.all())
    project_groups = []
    project_group = []
    count = 0

    for project in projects:
        project_group.append(project)
        count += 1
        if count == 3:
            project_groups.append(project_group)
            project_group = []
            count = 0
    if count != 0:
        project_groups.append(project_group)

    return render(request, "pages/projects.html", {
        "project_groups": project_groups,
    })


def project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    body_html = markdown.markdown(project.body)
    technologies_used = project.technology_used.all()
    return render(request, "pages/project.html", {
        "project": project,
        "body_html": mark_safe(body_html),
        "technologies_used": technologies_used,
    })


def contact(request):
    return render(request, "pages/contact.html")
