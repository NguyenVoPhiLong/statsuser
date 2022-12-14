from django.http import JsonResponse
from django.contrib.auth.models import User
from homepage.models import *


def user_check_checkbox(request):
    flag = True

    check_value = request.GET.get('check_value')
    userpk = request.GET.get('userpk')
    
    get_user = User.objects.get(pk = userpk)

    if check_value == 'on':
        get_user.is_active = True
        get_user.save()
        s = 'Kích hoạt'
        # status = 'true'
    else:
        get_user.is_active = False
        get_user.save()
        s = 'Chưa Kích hoạt'
        # status = 'false'

    
    if flag == True:
        data = {
            's': s,
            'flag': flag, 
        }
        return JsonResponse(data)
    else:
        data ={
            'flag': flag,
        }
        return JsonResponse(data)

def validate_username(request):
    username = request.GET.get('username')

    u_exist = User.objects.filter(username=username)
    flag = False

    if len(u_exist) > 0:
        flag = True
        data = {
            'flag': flag
        }
        return JsonResponse(data)
    else:
        data = {
            'flag': flag,
        }
        return JsonResponse(data)

def edit_user(request):
    id = request.GET.get('id')
    
    user = User.objects.filter(pk = id)
    flag = False

    if len(user) > 0:
        flag = True
        user  = user[0]
        account = Account.objects.get(userid = user.pk)
        typeacc = account.accounttypeid.id
        data = {
            'flag': flag,
            'username': user.username,
            'password': 'Nhập mật khẩu khác (nếu muốn)',
            'first_name': user.first_name,
            'last_name': user.last_name,
            'typeacc': typeacc
        }
        return JsonResponse(data)
    else:
        data = {
            'flag': flag,
        }
        return JsonResponse(data)