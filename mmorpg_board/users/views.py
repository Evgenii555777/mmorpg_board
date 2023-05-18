from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth import logout
from django.contrib import messages

def registration_success(request):
    return render(request, 'users/registration_success.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                send_confirmation_email(user)
                return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def send_confirmation_email(user):
    # Отправка письма с подтверждением регистрации
    subject = 'Подтверждение регистрации'
    message = 'Добро пожаловать на наш сайт! Ваша регистрация прошла успешно.'
    from_email = 'SkillFactoryTest@yandex.ru'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

def logout_view(request):
    logout(request)
    return redirect('post_list')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                messages.error(request, 'Неправильное имя пользователя или пароль.')
    return render(request, 'users/login.html')
