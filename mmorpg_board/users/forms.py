from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render, redirect

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
            send_confirmation_email(user)

        return user

def send_confirmation_email(user):
    subject = 'Подтверждение регистрации'
    message = 'Добро пожаловать на наш сайт! Пожалуйста, подтвердите свою регистрацию.'
    from_email = 'SkillFactoryTest@yandex.ru'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
