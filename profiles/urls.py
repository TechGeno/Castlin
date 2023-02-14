from django.urls import path,include
from . import views

urlpattern=[
    path('profile',views.profiles,name='profile'),
]