from django.forms import (
    ModelForm, CharField, IntegerField,
)
from viewer.models import Movie
from viewer.validators import PastMonthField, capitalized_validator

from django.core.exceptions import ValidationError

import re

class MovieForm(ModelForm):
    class Meta: #subklasa opisująca dane z których będzie tworzony form
        model = Movie #model na podstawie tworzymy formularz
        fields = '__all__' #wykorzystujemy wszystkie pola z modelu

    #pola z własnymi walidatorami dodajemy oddzielnie poza META
    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        # pobranie wartości pola description
        initial = self.cleaned_data['description']
        # podział teksu na części "od kropki do kropki" - na zdania
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        # zamiana na wielką literę pierwszej litery każdego ze zdań,
        # dodanie kropki, powtórzenie operacji dla kolejnego zdania
        return '. '.join(sentence.capitalize() for sentence in sentences)


    def clean(self):
        result = super().clean()
        if result['genre'].name == 'comedy' and result['rating'] > 7:
            # oznaczenie pola jako błędne bez komentarza
            self.add_error('genre', '')
            self.add_error('rating', '')
            # rzucamy ogólny błąd / wyjątek
            raise ValidationError(
                'Commedies aren\'t so good to be over 7'
            )
        return result
