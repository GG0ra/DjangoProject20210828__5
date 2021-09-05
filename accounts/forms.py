from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)

from django.forms import CharField, Form, Textarea  # <== NOWE

from accounts.models import Profile

from django.db.transaction import atomic


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = CharField(
        label='Opowiedz o sobie', widget=Textarea, min_length=30
    )  # <===NOWE

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=result)
        if commit:
            profile.save()
        return result
