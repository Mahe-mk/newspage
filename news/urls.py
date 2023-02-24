from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from news import views
from.views import Home,All_news,Categories,AllCategory,Detail,Category,SignUpView,WeatherView


urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('all-news',All_news.as_view(),name='all-news'),
    path('detail/<int:id>',Detail.as_view(),name='detail'),
    path('all-category',AllCategory.as_view(),name='all-category'),
    path('category/<int:id>',Category.as_view(),name='category'),
    path('signin', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout', auth_views.LogoutView.as_view(template_name='signout.html'), name='signout'),
    path('signup',SignUpView.as_view(),name='signup'),
    path('weather',WeatherView.as_view(),name='weather'),
    path("", include("allauth.urls")),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

