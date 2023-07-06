from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import News, Categories,UsersFavoriteCategory,ExtraField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm
from django.http import HttpResponse,JsonResponse
from google_auth_oauthlib.flow import Flow
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authentication import SessionAuthentication
from django.views import View
from django.views.generic import ListView
from.serializers import NewsSerializer,UserSerializer,CategoriesSerializer
from dateutil import parser
import requests,os
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication


# Home Page
class Home(APIView):
    def get(self, request, *args, **kwargs):
        first_news = News.objects.first()
        three_news = News.objects.all()[1:3]
        three_categories = Categories.objects.all()[0:3]
        data = {
            'first_news': NewsSerializer(first_news).data,
            'three_news': NewsSerializer(three_news, many=True).data,
            'three_categories': []
        }
        for category in three_categories:
            news = News.objects.filter(category=category)[:3]
            category_data = {
                'id': category.id,
                'title': category.title,
                'news': NewsSerializer(news, many=True).data
            }
            data['three_categories'].append(category_data)  
        return Response(data, status=status.HTTP_200_OK)


# Fetch and display the list of all_news
class All_news(APIView):
    def get(self, request):
        all_news = News.objects.all()
        serializer = NewsSerializer(all_news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    


# Fetch the detailed full news    
class Detail(APIView):
    def get(self, request, id):
        news = get_object_or_404(News, id=id)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Fetch all category 
class AllCategory(APIView):
    def get(self, request):
        cats = Categories.objects.all()
        serializer = CategoriesSerializer(cats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Fetch all news from selected category
class Category(APIView):
    def get(self, request, id):
        category = get_object_or_404(Categories, id=id)
        news = News.objects.filter(category=category)
        serializer = NewsSerializer(news, many=True)
        return Response({
            'all_news': serializer.data,
            'categories': CategoriesSerializer(category).data
        }, status=status.HTTP_200_OK) 
    
# To signup the user        
class SignUpView(APIView):
    def get(self, request):
        form = UserRegistrationForm()
        context = {'form': form}
        # return render(request, 'signup.html', context)
        return JsonResponse(context)
    def post(self, request):
        form = UserRegistrationForm(data=request.data)
        if form.is_valid():
            form.save()
            # return JsonResponse({'success': True},status=status.HTTP_201_CREATED)
            return redirect('http://127.0.0.1:3000/signin')
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
                
#To Signin the user for login    
class SignInView(APIView):
    def get(self, request):
        form = AuthenticationForm()
        context = {'signin_form': form} 
        return render(request, 'signin.html', context)
    @csrf_exempt
    def post(self, request):
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                token = str(refresh.access_token)
                print("Generated token:", token)
                return Response({'success': True,'token': token})
            else:
                form.add_error(None, "Invalid username or password.")
        errors = dict(form.errors.items())
        return Response({'success': False, 'errors': errors}, status= status.HTTP_400_BAD_REQUEST)
          
# To Signout the  user   
class SignOutView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)  
    @csrf_exempt  
    def post(self, request):     
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)


# Weather Report
class WeatherView(APIView):
    def get(self, request):
        api_key = os.getenv('API_KEY')
        city = "Madurai"
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(api_url)
        weather_data = response.json()
        return Response(weather_data, status=200)

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
                return redirect('http://127.0.0.1:3000/')
        return redirect('http://127.0.0.1:3000/signin')
    

# To view the User's Favourite Category
class MyCategoriesView(ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return []
        user = self.request.user
        favorite_categories = UsersFavoriteCategory.objects.filter(user=user)
        fav_news = News.objects.filter(category__in=favorite_categories.values_list('category'))
        return fav_news   
