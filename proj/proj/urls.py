"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

import base_app.views as base_views
import people_app.views as people_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", base_views.index),
    path("about", base_views.about),
    path("links", base_views.links),
    path("people", base_views.people),
    path("people/<uuid:id>/", base_views.people_id),
    path("people/api/", include("people_app.urls")),
]
