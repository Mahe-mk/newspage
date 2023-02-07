django-admin startproject todolist
cd todowoo
python manage.py startapp tasks
#open project to pycharm
#add the created app 'tasks' to project settings installed_apps
python manage.py runserver
#if u notice unapplied migrations
then apply migrations
python manage.py migrate
python manage.py runserver

--- create signup form -- for user to register in our site

IN project Urls.py

from todo import views
#add urls  -- add url for signup page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register')
]

todo views.py
#Now we will use a form for user registration
# we can use the builitin module from contrib

from django.contrib.auth.forms import UserCreationForm

#update the view to render a user signup form
def register(request):
    return render(request, 'tasks/register.html', {'form': UserCreationForm()})

Now we can use the instance of UserCreationForm in template
# All we have to do is just bind the from context

user signup form becomes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register With Us</title>
</head>
<body>
 User Singup Page
{{ form }}
</body>
</html>
python manage.py migrate
 
python manage.py runserver

# update content to allow csrf and add submit button

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register With Us</title>
</head>
<body>
<h1> User Singup Page </h1>
<form method ='post'>
    {% csrf_token %} <!-- cross site resource forgery -->
    {{ form.as_p }}
    <br>
    <input type="submit" value="Register User"></input>
</form>
</body>
</html>


update the view for get and post methods
-- when user is posting create the user
-- when the user requesting render the registration form
-- import the user model from django contrib


-- update the template for a success message
-- also send the success message via view
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register User</title>
</head>
<body>
<form method ='post'>

{% csrf_token %}
{{ form.as_table }}
<br>
<input type="submit" value="Register User"></input>
<!-- as_ul, as_p, as_table -->
</form>
<br>
{{ Message }}
</body>
</html>


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if(request.method == 'GET'):
        return render(request, 'tasks/register.html', {'form': UserCreationForm()})
    else:
        if(request.POST['password1'] ==  request.POST['password2']):
            user = User.objects.create_user(request.POST['username'], request.POST['password1'])
            user.save()
            return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'User Created Successfully'})

Handling the Integrity Error (Uniqueness of User)
Duplicating User will throw Integrity error

#Handling Error Pages
from django.db import IntegrityError

# Create your views here.
def register(request):
    if(request.method == 'GET'):
        return render(request, 'tasks/register.html', {'form': UserCreationForm()})
    else:
        try:
            if(request.POST['password1'] ==  request.POST['password2']):
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'User Created Successfully'})
        except IntegrityError:
            return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'UserName Already Exists, Please choose a different Name'})

-- if user already exists
   --     return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'UserName Already Exists, Please choose a different Name'})

-- lets handle the password mismatch
-- if passwords dont match render the template with different message
-- return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message':'Passwords Do Not Match'})



-- when the user creation is successful instead of giving message login the user and redirect the user to home page,
for login the user use the login method from contrib

from django.contrib.auth import login, logout, authenticate
-- update the view with the below lines instead of showing the success message

login(request,user)
return redirect('home')

-- this will be the home view function
def home(request):
    return render(request, 'tasks/home.html')

register view is updated with login and redirect methods
# Create your views here.
def register(request):
    if(request.method == 'GET'):
        return render(request, 'tasks/register.html', {'form': UserCreationForm()})
    else:
        try:
            if(request.POST['password1'] == request.POST['password2']):
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
                #return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'User Created Successfully'})
            else:
                return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'Passwords Do Not Match'})
        except IntegrityError:
            return render(request, 'tasks/register.html', {'form': UserCreationForm(), 'Message': 'UserName Already Exists, Please choose a different Name'})


def home(request):
    return render(request, 'tasks/home.html')

-- we will also add the template for the home task

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
hello world
</body>
</html>


-- redirect will not work as we have not added the path to the urls.py
-- so add the path to the urls.py for home
--- path('home/', views.home, name='home'),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]


Since we have redirected the successful registered user, the message will always be errors only so we can highlight the error message with a bit of css
In template add binding to the 'Error'

<h4 style="color:red"> {{ Message }} </h4>

Now we have created all the functionality for registration, lets go ahead and create the functionality for login

login from view
from django.contrib.auth import login


#redirect after login
from django.shortcuts import render, redirect
                login(request, user)
                return redirect('home')

def currenttodos(request):
    return render(request, 'tasks/home.html')

also add path to urls
path('home/', views.home, name='home'),

show if a user is logged in
add new template
base.html

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
we will use extending to extend specific portion of page from an common parts of page

to show the common content across different pages we will use base.html
this will be extending any specific user content based page..
so the base.html will be acting like a theme.


-- add new template inside tasks folder base.html

now if the user is already logged in lets show them they are logged in already also provide logout option
if they not logged in we can provide links to register on sign in page.
qaaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa~!!!!!!!!!!!!!!!!!!
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to Todos</title>
</head>
<body>
{% if user.is_authenticated %} <!-- if condition checks if user is already logged in and then displays a differnt html -->
 Logged in as {{ user.username }}
<a href="#">Logout</a>
{% else %} <!-- if the user is not logged in already we are displaying controls for him to login or register -->
<a href="#">Login</a>
<a href="#">Register</a>
{% endif %}

<!-- content block 1 -->
{% block content %}

{% endblock %}
<!-- content block 2 -->
<!-- add as many content blocks you need for clarity -->
{% block foot %}

{% endblock %}

</body>
</html>


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
we will have to extend the home.html to display the generic content that is available from the base.html

{% extends 'tasks/base.html' %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
{% block content %}
<h4> welcome to todosite</h4>
<h5> we aim at making reminders for your todolist here </h5>
{% endblock %}

{% block foot %}
<p>&#169; This page developed by Balaji Dileep Kumar</p>
{% endblock %}
</body>
</html>
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Also extend the register page so that it shows a user is already signed in/Logged in .
--register.html

{% extends 'tasks/base.html' %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register User</title>
</head>
<body>
{% block signup %}
<form method ='post'>
{% csrf_token %}
{{ form.as_table }}
<br>
<input type="submit" value="Register User"></input>
<!-- as_ul, as_p, as_table -->
</form>
<br>
<h4 style="color:red"> {{ Message }} </h4>
{% endblock %}
</body>
</html>

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Lets add the option to logout to enable the new user to signup or register

--add logout option
add path to logout in urls.py
    path('logout/', views.logoutuser, name='logout'),

add the corresponding view

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

if the user is already registered we need page for him to login with his credentials.
so add a login page.
first add route for login, similar to logout we dont use login as view function name as its already being used by contrib.auth login method

 path('login/', views.loginuser, name='login')
login.html
{% extends 'todo/base.html' %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home Page</title>
</head>
<body>
{% block content %}
<br>
<br>
Home Page content
{% endblock %}
</body>
</html>

add login view