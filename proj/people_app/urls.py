from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_root),
    path("<uuid:id>/", views.get_person_by_id),
]
