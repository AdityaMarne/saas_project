from django.shortcuts import render
from django.contrib.auth import authenticate,login

# Create your views here.
def login_view(request):
    username = "aditya" #request.POST['username']
    password = "123456" #request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("Login Here")
    return render(request, "auth/login.html",{})
