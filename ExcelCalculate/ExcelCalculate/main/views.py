from django.shortcuts import render, redirect
from random import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def signup(request):
    return render(request, 'main/signup.html')

def join(request):
    print(request)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name=name, user_email=email, user_password=pw)
    user.save()
    code = randint(1000, 9999)
    return redirect('main_verifyCode')

def signin(request):
    return render(request, 'main/signin.html')

def VerifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    return render(request, 'main/result.html')