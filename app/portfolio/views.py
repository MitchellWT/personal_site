import markdown
from django.shortcuts import get_object_or_404, render
from django.utils.safestring import mark_safe

from .models import About, Project, Picture


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
    projects = list(Project.objects.all().order_by("-id"))
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


def pictures(request, page=1):
    perPage = 5
    limit = page * perPage
    offset = (page - 1) * perPage
    pictures = list(Picture.objects.order_by("-taken_date")[offset:limit])
    totalCount = Picture.objects.count()
    prev = 0 if offset < 1 else page - 1
    next = 0 if limit >= totalCount else page + 1
    return render(request, "pages/pictures.html", {
        "pictures": pictures,
        "page": page,
        "prev": prev,
        "next": next
    })


def picture(request, slug):
    picture = get_object_or_404(Picture, slug=slug)
    subjects = picture.subjects.all()
    return render(request, "pages/picture.html", {
        "picture": picture,
        "subjects": subjects
    })


def error_404(request, exception):
    return render(request, "errors/catch_all.html", {
        "error_code": "404",
        "description": "Sorry it looks like that page doesn't exist!",
    }, status=404)


def error_500(request):
    return render(request, "errors/catch_all.html", {
        "error_code": "500",
        "description": "Sorry it looks like our system is having some issues!",
    }, status=500)


def error_403(request, exception):
    return render(request, "errors/catch_all.html", {
        "error_code": "403",
        "description": "Sorry it looks like you don't have permission to access that!",
    }, status=403)


def error_400(request, exception):
    return render(request, "errors/catch_all.html", {
        "error_code": "400",
        "description": "Sorry it looks like your request was bad!",
    }, status=400)
