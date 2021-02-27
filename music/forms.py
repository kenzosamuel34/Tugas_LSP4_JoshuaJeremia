from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Song, Profile

#Untuk Menyimpan Data SongForm
class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'genre', 'singer', 'rating']

#Untuk Menyimpan Data Singup
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    gender = forms.ChoiceField(widget=forms.Select, choices=gender_choices)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender',
                  'email', 'username', 'password1', 'password2']
