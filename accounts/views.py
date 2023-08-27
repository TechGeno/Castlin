from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import os
# Create your views here.

# logging out
def logout(request):
    auth.logout(request)
    return redirect('/')


# validating login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
#for authenticating if the user is authentic
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
            
    else:
        return render(request, 'login.html' )

#registering accounts
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if (password1==password2 and len(password1)>=8):
            if User.objects.filter(username=username).exists():
                messages.info(request , 'Username is already taken please choose another one')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request , 'An account is already associated with the given email address please try logging in instead')
                return redirect('register')
            #file creation part for each user made :-)
            else:
                user = User.objects.create_user(username=username,email=email,password = password2)
                a=str(username)+'.txt'
                current_directory = os.path.dirname(os.path.abspath(__file__))
                user_data_directory = os.path.join(current_directory, "Users data")
                os.makedirs(user_data_directory, exist_ok=True)
                filepath = os.path.join(user_data_directory, a)
                # filepath = f"C:\\Users\\SriHarsha\\Desktop\\Castlin\\Users data\\{a}"
                f = open(filepath, 'w')
                f.write('Username : '+ username +'\n')
                f.write('Email ID : '+ email + '\n') 
                f.write('Password : '+ password1 + ' ')
                f.close()
                user.save()
                return redirect('login')    
        if (len(password1)<8):
            messages.info(request,'Password must contain atleast 8 characters')
        else:
            messages.info(request , 'Both the passwords did not match please try again')
            return redirect('register')
    else:
        return render(request, 'register.html' )


def signup_redirect(request):
    messages.error(request,"Something went wrong here, It maybe that you already have account!")
    return redirect('login')
