from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
# Create your views here.

def sendEmail(request):
    check_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    print(check_res_list, "/", inputReceiver, "/", inputTitle, "/", inputContent)
    return HttpResponseRedirect(reverse('index'))

