from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from news import views


urlpatterns=[
    path('',views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('signin', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout', auth_views.LogoutView.as_view(template_name='signout.html'), name='signout'),
    path('signup',views.signup,name='signup'),
    path('weather',views.weather,name='weather'),
    path("", include("allauth.urls")),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

