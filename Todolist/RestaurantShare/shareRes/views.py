from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    # return HttpResponse('index')
    return render(request, 'shareRes/index_init.html')

def restaurantDetail(request):
    # return HttpResponse('restaurantDetail')
    return render(request, 'shareRes/restaurantDetail_init.html')

def restaurantCreate(request):
    # return HttpResponse('restaurantCreate')
    return render(request, 'shareRes/restaurantCreate_init.html')

def categoryCreate(request):
    # return HttpResponse('categoryCreate')
    return render(request, 'shareRes/categoryCreate_init.html')