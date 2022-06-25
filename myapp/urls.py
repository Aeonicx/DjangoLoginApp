from django.urls import path
from .views import *

urlpatterns= [
    path('', index),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('dashboard', dashboard, name='dashboard'),
    path('registration', registration, name='registration'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
]