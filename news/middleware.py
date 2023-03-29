from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            if request.user.is_authenticated or request.path in [reverse('signin'), reverse('signup'), reverse('google_login')]:
                return self.get_response(request)
            return redirect('signin')