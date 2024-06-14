from django.shortcuts import get_object_or_404
from people_app.models import Person


def RequestPersonById(id):
    return get_object_or_404(Person, _id=id)
