"""repo_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html'), name="home"),
    # path('users/', include('users.urls')),
    path('', include("reddit.urls")),
    path('', include("users.urls")),
]
