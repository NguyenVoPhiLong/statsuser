from django.urls import path
from homepage.views import *

app_name = 'homepage'

urlpatterns = [
    path('index', index, name='index'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('signout', signout, name='signout'),
]