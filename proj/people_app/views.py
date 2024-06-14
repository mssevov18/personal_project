from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import uuid

from people_app.models import Person
from people_app.controls import *


@csrf_exempt
def api_root(request):
    match request.method:
        case "GET":
            people = list(
                Person.objects.values()
            )  # Convert QuerySet to list of dictionaries
            return JsonResponse(people, safe=False)  # Return JSON response

        case "POST":
            try:
                data = json.loads(request.body)
                person = Person.objects.create(
                    first_name=data["first_name"],
                    middle_name=data["middle_name"],
                    last_name=data["last_name"],
                    birthdate=data["birthdate"],
                    emails=data["emails"],
                    discord=data["discord"],
                    steam=data["steam"],
                    battlenet=data["battlenet"],
                    instagram=data["instagram"],
                    facebook=data["facebook"],
                    github=data["github"],
                    leagueoflegends=data["leagueoflegends"],
                )
                return JsonResponse(
                    {"message": "Person created", "id": person._id}, status=201
                )
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)


def get_person_by_id(request, id):
    return JsonResponse(RequestPersonById(id).to_json())
