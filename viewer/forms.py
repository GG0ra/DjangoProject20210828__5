from django.core.exceptions import ValidationError
from django.forms import (
    Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea
)
from viewer.models import Genre

from viewer.validators import PastMonthField, capitalized_validator

import re


class MovieForm(Form):
    title = CharField(max_length=128)  # input - max: 128
    genre = ModelChoiceField(queryset=Genre.objects)  # select -> options (pojedynczy wiersz z Genre)
    rating = IntegerField(min_value=1, max_value=10)  # input type: number, min=1, max=10
    released = PastMonthField()  # input type: date
    description = CharField(widget=Textarea, required=False)  # nie będzie wymagane

    def clean_description(self):
        #pobranie wartości pola description
        initial = self.cleaned_data['description']
        #podział textu na częsci "od kropki do kropki" na zdania
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        #zamiana na wielką literę pierwszej litery każdego zdania
        #dodanie kropki, powtórzenie operacji dla kolejnego zdania
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'comedy' and result['rating'] > 7:
            #oznaczenie polajako błędne bez komentarza
            self.add_error('genre', '')
            self.add_error('rating', '')
            #rzucamy ogólny błąd/wyjątek
            raise ValidationError('Comedies aren\'t so good to be over 7')
        return result
