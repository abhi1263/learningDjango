from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label or 'Username'
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = self.fields['password1'].label or 'Username'
        self.fields['password2'].widget.attrs['placeholder'] = self.fields['password2'].label or 'Username'