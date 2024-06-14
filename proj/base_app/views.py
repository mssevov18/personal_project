from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from people_app.models import Person, PersonQueryToJson
from people_app.controls import *


# Create your views here.
def index(request):
    return render(request, "base_app/index.html")


def about(request):
    return render(request, "base_app/about.html")


def links(request):
    return render(request, "base_app/links.html")


def people(request):
    return render(
        request,
        "base_app/people.html",
        context={"people": PersonQueryToJson(Person.objects.all())},
    )


def people_id(request, id):
    # try:
    person = RequestPersonById(id)
    return render(
        request, "people_app/person_details.html", context={"person": person.to_json()}
    )


# except Exception as e:
# return HttpResponse(f"Exception caught {type(e)}. {e}")
