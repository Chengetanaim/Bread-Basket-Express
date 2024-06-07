from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields["username"].widget.attrs.update({'placeholder': 'Username'})
        self.fields["password"].widget.attrs.update({'placeholder': 'Password'})

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields["username"].widget.attrs.update({'placeholder': 'Username'})
        self.fields["password1"].widget.attrs.update({'placeholder': 'Password'})
        self.fields["password2"].widget.attrs.update({"placeholder": "Confirm Password"})