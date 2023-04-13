from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import News, Categories,UsersFavoriteCategory,ExtraField
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm
from django.http import HttpResponse,JsonResponse
from google_auth_oauthlib.flow import Flow
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.views.generic import ListView
from.serializers import NewsSerializer,UserSerializer,CategoriesSerializer
from dateutil import parser
import requests,os
from google.oauth2 import id_token
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

# Fetch and display the list of all_news

class All_news(View):
    def get(self, request):
        all_news=News.objects.all()
        return render(request, 'all-news.html', {
            'all_news': all_news
        })  
    
def allNews(request):
    allNews = News.objects.all()
    data = {'allNews': [{'title': News.title, 'detail': News.detail} for news in allNews]}
    return JsonResponse(data)
     

# Fetch the detailed full news 
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
    
# class AllCategory(View):  
#     def get(self, request):
#         cats = Categories.objects.all()
#         data = [{'id': cat.id, 'title': cat.title, 'category_image': cat.category_image.url} for cat in cats]
#         return JsonResponse({'categories': data})    

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
        api_key = os.getenv('API_KEY')
        city = "Madurai"
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(api_url)
        weather_data = response.json()
        return render(request, "weather.html", {"weather_data": weather_data})


# To Authenticate the user with Google account
class GoogleLogin(View):
    def get(self, request):
        client_id = os.getenv('CLIENT_ID')
        redirect_uri = 'http://127.0.0.1:8000/google/login/callback/'
        scope = ['https://www.googleapis.com/auth/userinfo.email', 
                 'https://www.googleapis.com/auth/userinfo.profile',
                 'https://www.googleapis.com/auth/user.phonenumbers.read',
                 'https://www.googleapis.com/auth/user.addresses.read',
                 'https://www.googleapis.com/auth/user.birthday.read',
                 ]
        auth_url = 'https://accounts.google.com/o/oauth2/v2/auth?' + \
            f'client_id={client_id}&' + \
            f'redirect_uri={redirect_uri}&' + \
            f'scope={" ".join(scope)}&' + \
            f'response_type=code'
        return redirect(auth_url)
    
# To redirect the URL after getting the auth_code from API  
class AuthRedirect(View):
    def get(self, request):
        token_url = 'https://oauth2.googleapis.com/token'
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        redirect_uri = 'http://127.0.0.1:8000/google/login/callback/'
        code = request.GET.get("code")
        params = {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        }
        response = requests.post(token_url, data=params)
        token_data = response.json()
        access_token = token_data.get('access_token')
        if access_token:
            profile_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
            people_url = 'https://people.googleapis.com/v1/people/me?personFields=phoneNumbers,addresses,birthdays'
            headers = {'Authorization': f'Bearer {access_token}'}
            profile_response = requests.get(profile_url, headers=headers)
            people_response = requests.get(people_url, headers=headers)
            profile_data = profile_response.json()
            email = profile_data.get('email')
            name = profile_data.get('name')
            people_data = people_response.json()
            phone_number = None
            if 'phoneNumbers' in people_data:
                phone_number = people_data['phoneNumbers'][0]['value']
            addresses = None    
            if 'addresses' in people_data:
                addresses = people_data['addresses'][0]['formattedValue']
            birthdays = None    
            if 'birthdays' in people_data:
                birthdays = people_data['birthdays'][0]['date']   
            if email:
                first_name = name.split()[0]
                try:
                    user = User.objects.get(email=email)
                    user.first_name = first_name
                    user.save()
                    extra_field = ExtraField.objects.get(user=user)
                    extra_field.phone_number = phone_number
                    extra_field.addresses = addresses
                    extra_field.birthdays = birthdays
                    extra_field.save()
                except User.DoesNotExist:
                    user = User.objects.create_user(first_name, email=email, first_name=first_name)
                    extra_field = ExtraField.objects.create(user=user,phone_number=phone_number,addresses=addresses, birthdays=birthdays)
                login(request, user)
                return redirect('home')
        return redirect('signin')


# To create an Personalized view for user    
class MyCategoriesView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'Fav_Categories.html'
    context_object_name = 'fav_news'
    def get_queryset(self):
        username = self.request.user.username
        username = User.objects.get(username=username)
        favorite_categories = UsersFavoriteCategory.objects.filter(user=username)
        fav_news = News.objects.filter(category__in=favorite_categories.values_list('category'))
        return fav_news


def index(request):
    return render (request, 'index.html')

class NewsAPIView(APIView):
    def get(self, request):
        news=News.objects.all()
        serializer= NewsSerializer(news, many= True)
        return Response(serializer.data)
