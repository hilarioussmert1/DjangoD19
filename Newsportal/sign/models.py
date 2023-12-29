from datetime import datetime
from django.db import models
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = ('username',
                  'name',
                  'surname',
                  'email',
                  'password1',
                  'password2',)


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user

