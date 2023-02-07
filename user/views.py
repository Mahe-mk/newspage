from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    return render(request,"index.html")


def signup(request):
    
    if(request.method == 'GET'):
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
            if(request.POST['password1'] == request.POST['password2']):
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                signin(request, user)
                return redirect('home')
                #return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'User Created Successfully'})
            else:
                return render(request, 'signup.html', {'form': UserCreationForm(), 'Message': 'Passwords Do Not Match'})

def signin(request):
    return render(request, 'signin.html')


def signout(request):
    return render(request, 'signout.html')
    