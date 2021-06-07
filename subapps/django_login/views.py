#Librairies for Login
from django.contrib.auth import login as auth_login,logout as auth_logout, authenticate
from django.shortcuts import render,redirect
from .forms import LoginForm

import logging
logger = logging.getLogger('django_login')


def login(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # user.profile.set_session_key(request.session.session_key)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                logger.info("User {0} connected successfully to database".format(username))
                return redirect('index')
            else:
                logger.warning('Wrong user ({0}) or password'.format(username))
                message = "Wrong Username/Password"
    else:
        form = LoginForm()
    return render(request, 'login.html', {'message':message, 'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')
