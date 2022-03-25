from django.forms import ModelForm
from .models import list, item
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ItemForm (ModelForm):
    class Meta:
        model = item
        fields = ('name',)


class ListForm (ModelForm):
    class Meta:
        model = list
        fields = ('name',)


class LoginForm (forms.Form):
    username = forms.CharField (label='', required=True, widget=forms.TextInput (attrs={'placeholder': 'Username'}))
    password = forms.CharField (label='', widget=forms.PasswordInput (attrs={'placeholder': 'Password'}),
                                required=True)




class UserRegistration (forms.ModelForm):
    username = forms.CharField (label='', required=True, widget=forms.TextInput (attrs={'placeholder': 'Username'}))
    first_name = forms.CharField (label='', required=True,
                                  widget=forms.TextInput (attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField (label='', required=True,
                                 widget=forms.TextInput (attrs={'placeholder': 'Last Name'}))
    # email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder', 'johndoe@example.com'}))
    email = forms.CharField (label='', max_length=100,
                             widget=forms.EmailInput
                             (attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField (label='', widget=forms.PasswordInput (attrs={'placeholder': 'Password'}),
                                required=True)
    password2 = forms.CharField (label='',
                                 widget=forms.PasswordInput (attrs={'placeholder': 'Verify Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError ('Passwords don\'t match.')
        return cd['password2']
