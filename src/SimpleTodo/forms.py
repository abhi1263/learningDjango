from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.utils import ErrorList


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label or 'Username'
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = self.fields['password1'].label or 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = self.fields['password2'].label or 'Confirm Password'


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])
