from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
# Create your views here.

def index(request):
    # return HttpResponse('index')
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/index_init.html', content)

def restaurantDetail(request):
    # return HttpResponse('restaurantDetail')
    return render(request, 'shareRes/restaurantDetail_init.html')

def restaurantCreate(request):
    # return HttpResponse('restaurantCreate')
    return render(request, 'shareRes/restaurantCreate_init.html')

def categoryCreate(request):
    # return HttpResponse('categoryCreate')
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/categoryCreate_init.html', content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("여기서 카테고리 기능 구현")

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))
    