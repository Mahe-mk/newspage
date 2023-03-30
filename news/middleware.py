from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response
        def __call__(self, request):
            if request.path in [reverse('home'),
                                reverse('all-news'), reverse('all-category'), 
                                reverse('weather'), reverse('Fav_Category')]:
                if request.user.is_authenticated:
                    return self.get_response(request)
                else:
                    return redirect('signin')
            else:
                return self.get_response(request)
