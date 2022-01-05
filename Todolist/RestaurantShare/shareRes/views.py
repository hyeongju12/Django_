from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
# Create your views here.

def index(request):
    # return HttpResponse('index')
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories' : categories, 'restaurants' : restaurants}
    return render(request, 'shareRes/index_init.html', content)

def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant' : restaurant}
    # return HttpResponse('restaurantDetail')
    return render(request, 'shareRes/restaurantDetail_init.html', content)

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    # return HttpResponse('restaurantCreate')
    return render(request, 'shareRes/restaurantCreate_init.html', content)

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category=category, restaurant_name = name, 
                            restaurant_link = link, restaurant_content = content,
                                restaurant_keyword = keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories' : categories, 'restaurant' : restaurant}
    return render(request, 'shareRes/restaurantUpdate_init.html', content)

def Update_restaurant(request):
    resId = request.POST['resId']
    ch_category_id = request.POST['resCategory']
    ch_category = Category.objects.get(id = ch_category_id)
    ch_name = request.POST['resTitle']
    ch_link = request.POST['resLink']
    ch_content = request.POST['resContent']
    ch_keyword = request.POST['resLoc']
    b_restaurant = Restaurant.objects.get(id=resId)
    b_restaurant.category = ch_category
    b_restaurant.name = ch_name
    b_restaurant.link = ch_link
    b_restaurant.content = ch_content
    b_restaurant.keyword = ch_keyword
    b_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id' : resId}))

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
    