from django.urls import path
from adminpage.views import *
from adminpage.ajax import *

app_name = 'adminpage'

urlpatterns = [
    path('', index, name='index'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('signout', signout, name='signout'),

    path('users', users, name='users'),
    path('user_check_checkbox', user_check_checkbox, name='user_check_checkbox'),
    path('user_delete/<int:id>', user_delete, name='user_delete'),

    path('validate/username', validate_username, name='validate_username'),
    path('edit/user', edit_user, name='edit_user'),
]