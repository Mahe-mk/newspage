from django.contrib import admin
from django.urls import path,include
from user import views


urlpatterns = [
    path('index',views.index,name='index'),
    path('singin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('signup',views.signup,name='signup'),
    
]