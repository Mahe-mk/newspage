from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from news import views
urlpatterns=[
    path('',views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('singin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('signup',views.signup,name='signup'),
] 