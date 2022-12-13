from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from datetime import datetime
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('homepage:login')

    context = {

    }

    return render(request, 'homepage/index.html', context)


def signin(request):
    if not request.user.is_authenticated:
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('homepage:index')

            return redirect('homepage:login')
        return redirect('homepage:login')
    else:
        return redirect('homepage:login')

def signup(request):
    if not request.user.is_authenticated:
        username = request.GET.get('username', None)
        password1 = request.GET.get('password1', None)
        password2 = request.GET.get('password2', None)

        if username == None and password1 == None and password2 == None:
            return render(request, 'homepage/signup.html')
        if password1 != password2:
            return render(request, 'homepage/signup.html')

        new_user = User()
        new_user.username = username
        new_user.set_password(password1)
        new_user.date_joined = datetime.now()
        new_user.is_active = True
        new_user.save()

        login(request, new_user)
        return redirect('homepage:index')
    else:
        return render(request, 'homepage/signup.html')

def signout(request):
    try:
        logout(request)
    except:
        pass
    return redirect("homepage:index")