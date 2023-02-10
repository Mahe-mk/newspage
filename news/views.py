from django.shortcuts import render,redirect
from django.contrib import messages
from .models import News, Categories
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# def signin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#     return render(request, 'signin.html', {})

# To Signin the user
def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="signin.html", context={"signin_form":form})

# To Signout the  user
def signout(request):
    logout(request)
    return render(request, 'signout.html')
