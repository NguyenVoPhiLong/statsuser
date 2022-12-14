from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from  datetime import datetime

from homepage.models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('adminpage:signin')
    
    context = {
        'is_login': 1,
    }

    return render(request, 'adminpage/index.html', context)

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            print(username, password)
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('adminpage:index')
                else:
                    return redirect('adminpage:signin')
            else:
                context = {
                    'mes': 'Tên đăng nhập hoặc mật khẩu không đúng!',
                }
                return render(request, 'adminpage/signin.html', context)
        return render(request, 'adminpage/signin.html')
    else:
        return redirect('adminpage:index')

def signup(request):
    if not request.user.is_authenticated:
        username = request.GET.get('username', None)
        password1 = request.GET.get('password1', None)
        password2 = request.GET.get('password2', None)

        if username == None and password1 == None and password2 == None:
            return render(request, 'adminpage/signup.html')
        if password1 != password2:
            return render(request, 'adminpage/signup.html')

        new_user = User()
        new_user.username = username
        new_user.set_password(password1)
        new_user.date_joined = datetime.now()
        new_user.is_active = True
        new_user.save()

        login(request, new_user)
        return redirect('adminpage:index')
    else:
        return render(request, 'adminpage/signup.html')

def signout(request):
    try:
        logout(request)
    except:
        pass
    return redirect("adminpage:index")

def users(request):
    if not request.user.is_authenticated:
        return redirect('adminpage:signin')


    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        typeacc = request.POST.get('typeacc')
        typeupdate = request.POST.get('type')

        if typeupdate == 0 or typeupdate == '0':
            user = User()
            user.username = username
            user.set_password(password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()

            account = Account()
            account.userid = user
            account.accounttypeid = AccountType.objects.get(id=typeacc)
            account.save()
        else:
            user = User.objects.get(pk=typeupdate)
            user.username = username
            if password != 'Nhập mật khẩu khác (nếu muốn)':
                user.set_password(password)
        
            user.last_name = last_name
            user.first_name = first_name

            account = Account.objects.get(userid = user.pk)
            account.accounttypeid = AccountType.objects.get(id=typeacc)

            user.save()
            account.save()

    users = User.objects.all()
    types = AccountType.objects.all()
    class userandtype:
        user = User()
        typeacc = AccountType()

    clsusers = []
    for user in users:
        cls = userandtype()
        cls.user = user
        try:
            account = Account.objects.get(userid = user.pk)
            cls.typeacc = account.accounttypeid
        except:
            cls.typeacc = AccountType.objects.get(id=1)

        clsusers.append(cls)

    context = {
        'is_login': 1,
        'clsuserss': clsusers,
        'types': types
    }

    return render(request, 'adminpage/users.html', context)

def user_delete(request, id):
    if not request.user.is_authenticated:
        return redirect('adminpage:signin')

    user = User.objects.get(pk=id)
    if request.method == 'POST':
        adminpass = request.POST.get('adminpass')
       
        if request.user.check_password(adminpass):
            try:
                account = Account.objects.get(userid = user.pk)
                account.delete()
                user.delete()
            except:
                pass
            
            return redirect('adminpage:users')
        else:
            return redirect('adminpage:users')
    context = {
        'is_login': 1,
    }

    return render(request, 'adminpage/users.html', context)