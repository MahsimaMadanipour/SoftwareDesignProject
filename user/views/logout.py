from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_user(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')
