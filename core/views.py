from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def login(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário e/ou senha inválidos. Tente novamente')

    return redirect('login')
