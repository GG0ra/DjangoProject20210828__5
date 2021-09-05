from django.db import models
from django.db.models import (Model,
                              CharField, DateField, DateTimeField, IntegerField, TextField,
                              ForeignKey, DO_NOTHING, )

# Create your models here.

class Genre(Model):
    name = CharField(max_length=128)


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)  # kiedy usuwamy film zostawiamy gatunek
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)  # zawsze bieżący czas
