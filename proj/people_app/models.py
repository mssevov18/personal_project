from django.db import models
import json
import uuid


class Person(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _datetimeAdded = models.DateTimeField(auto_now=True)
    _datetimeChanged = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    # picture
    emails = models.EmailField(max_length=254)
    phones = models.CharField(max_length=200, editable=False)
    discord = models.CharField(max_length=37)
    steam = models.CharField(max_length=32)
    battlenet = models.CharField(max_length=32)
    instagram = models.CharField(max_length=32)
    facebook = models.CharField(max_length=32)
    github = models.CharField(max_length=32)
    leagueoflegends = models.CharField(max_length=32)

    def set_phones(self, data):
        self.phones = json.dump(data)

    def get_phones(self):
        return json.loads(self.phones)

    def __str__(self):
        return f"{self._id} {self.first_name} {self.middle_name} {self.last_name}"

    def to_json(self):
        return {
            "id": self._id.__str__(),
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate.__str__(),
            "emails": self.emails,
            "discord": self.discord,
            "steam": self.steam,
            "battlenet": self.battlenet,
            "instagram": self.instagram,
            "facebook": self.facebook,
            "github": self.github,
            "leagueoflegends": self.leagueoflegends,
        }


def PersonQueryToJson(QuerySet):
    return [person.to_json() for person in QuerySet]
