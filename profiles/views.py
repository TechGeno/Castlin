from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def profile(request):
    #add the logic here for posting the information of the user