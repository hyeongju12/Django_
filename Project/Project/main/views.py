from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(reqeust):
    return render(reqeust, 'main/index.html')

def LoginView(request):
    return render(request, 'main/login.html')
    
