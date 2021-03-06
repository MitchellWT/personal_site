"""personal_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.conf.urls import include

import portfolio.views
from personal_site import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', portfolio.views.index),
    path('about/', portfolio.views.about),
    path('blog/', portfolio.views.blog),
    path('projects/', portfolio.views.projects),
    path('projects/<slug:slug>/', portfolio.views.project),
    path('pictures/', portfolio.views.pictures),
    path('pictures/<int:page>/', portfolio.views.pictures),
    path('picture/<slug:slug>/', portfolio.views.picture),
    path('contact/', portfolio.views.contact),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = portfolio.views.error_404
handler500 = portfolio.views.error_500
handler403 = portfolio.views.error_403
handler400 = portfolio.views.error_400
