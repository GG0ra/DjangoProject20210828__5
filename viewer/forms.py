from django.core.exceptions import ValidationError
from django.forms import (
    Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea, ModelForm
)
from viewer.models import Genre, Movie

from viewer.validators import PastMonthField, capitalized_validator

import re



class MovieForm(ModelForm):
    class Meta:  # subklasa opisująca dane z których będzie tworzony form
        model = Movie  # model na podstawie tworzymy formularz
        fields = '__all__'  # wykorzystujemy wszystkie pola z modelu

    # pola z własnymi walidatorami dodajemy oddzielnie, poza META
    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

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
