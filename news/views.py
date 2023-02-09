from django.shortcuts import render,redirect
from django.contrib import messages
from .models import News, Categories
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[1:3]
    three_categories=Categories.objects.all()[0:3]
    return render(request,'home.html',{
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories
    })

# All News
def all_news(request):
    all_news=News.objects.all()
    return render(request,'all-news.html',{
        'all_news':all_news
    })

# fetch the detailed full news 
def detail(request,id):
    news=News.objects.get(id=id)
    category=Categories.objects.get(id=news.category.id)
    return render(request,'detail.html',{
        'news':news,
    })


# Fetch all category 
def all_category(request):
    cats=Categories.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })

# Fetch all news from selected category
def category(request,id):
    category=Categories.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'categories':category
    })

# To Signup the user for login
# def Signup(request):
     
#     return render (request, 'signup.html')


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
  
    
    return render(request, 'signin.html')


def signout(request):
    return render(request, 'signout.html')


def signup(request):
    if(request.method == 'GET'):
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        try:
            if(request.POST['password1'] == request.POST['password2']):
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                signin(request,user)
                return redirect('home')
                #return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'User Created Successfully'})
            else:
                return render(request, 'signup.html', {'form': UserCreationForm(), 'Message': 'Passwords Do Not Match'})
        except IntegrityError:
            return render(request, 'signup.html', {'form': UserCreationForm(), 'Message': 'UserName Already Exists, Please choose a different Name'})
