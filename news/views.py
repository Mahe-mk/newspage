from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import News, Categories
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
import requests
# Create your views here.

class Home(View):
     def get(self, request, *args,**kwargs):
        first_news = News.objects.first()
        three_news = News.objects.all()[1:3]
        three_categories = Categories.objects.all()[0:3]
        context = {
            'first_news': first_news,
            'three_news': three_news,
            'three_categories': three_categories
        }
        return render(request, 'home.html', context)


class All_news(View):
    def get(self, request):
        all_news=News.objects.all()
        return render(request, 'all-news.html', {
            'all_news': all_news
        })
     
# fetch the detailed full news 

class Detail(View):
    def get(self, request, id):
        news = get_object_or_404(News, id=id)
        category = Categories.objects.get(id=news.category.id)
        return render(request, 'detail.html', {
            'news': news,
        })
        

# Fetch all category 

class AllCategory(View):
    def get(self, request):
        cats = Categories.objects.all()
        return render(request, 'category.html', {
            'cats': cats
        })
    

# Fetch all news from selected category

class Category(View):
    def get(self, request, id):
        category = get_object_or_404(Categories, id=id)
        news = News.objects.filter(category=category)
        return render(request, 'category-news.html', {
            'all_news': news,
            'categories': category
        })    
    
# To Signup the user for login

class SignUpView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            context = {'form': form}
            return render(request, 'signup.html', context)
        
# To Signin the user

class SignInView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {'signin_form': form}
        return render(request, 'signin.html', context)
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password.")
        context = {'signin_form': form}
        return render(request, 'signin.html', context)
    
# To Signout the  user
class SignOutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'signout.html')

# To display the weather report


class WeatherView(View):
    def get(self, request):
        api_key = "333a8faa57184ef5534e17ed15f5d342"
        city = "Madurai"
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(api_url)
        weather_data = response.json()
        return render(request, "weather.html", {"weather_data": weather_data})