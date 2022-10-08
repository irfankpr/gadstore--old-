from django.contrib import messages
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.decorators.cache import never_cache
from profiles.models import cart, userprofiles
from products.models import categories, sub_categories,products


# Create your views here.
def addcat(request):
    if request.method == 'POST':
        if request.POST['catname'] and request.POST['Description'] and request.FILES['catimage']:
            name = request.POST['catname']
            if categories.objects.filter(category_name=name).exists():
                messages.error(request, 'Category already exists !')
                return redirect('category')

            des = request.POST['Description']
            obj = categories()
            obj.category_name = name
            obj.description = des
            obj.slug = slugify(name)
            obj.category_image = request.FILES['catimage']
            obj.save()
            messages.error(request, 'New category added', extra_tags='added')
            return redirect('category')

        else:
            messages.error(request, 'fill all fields')
            return redirect('category')


def deletecat(request, catid):
    id = catid
    cat = categories.objects.get(id=id)
    name = cat.category_name
    categories.objects.filter(id=id).delete()
    sub_categories.objects.filter(parent_cat_id=id).delete()
    messages.error(request, 'Category  ' + name + ' and corresponding sub-categories deleted !')
    return redirect('category')


def addsubcat(request):
    if request.POST['cat'] and request.POST['subcat']:
        cat = request.POST['cat']
        subcat = request.POST['subcat']
        obj = sub_categories()
        obj.sub_cat_name = subcat
        obj.slug = slugify(subcat)
        obj.parent_cat_id = cat
        obj.save()
        messages.error(request, 'New sub category ' + subcat + " added.")
        return redirect('category')
    else:
        messages.error(request, 'field must filled')
        return redirect('category')


def addto_cart(request, id):
    if request.user.is_authenticated:
        obj = cart()
        if cart.objects.filter(user_id=request.user.id, product_id=id).exists():
            cart.objects.filter(user_id=request.user.id, product_id=id).update(count=F('count') + 1)
            return redirect('/')
        else:
            obj.user_id = request.user.id
            obj.product_id = id
            obj.save()
            return redirect('/')


def cart_dlt(request, id):
    if request.method == 'GET':
        cart.objects.get(id=id).delete()
        return redirect('cartv')


def cart_count(request):
    if request.method == 'GET':
        c=request.GET['count']
        id=request.GET['cart']
        cart.objects.filter(id=id).update(count=F('count') + c)
        cart.objects.filter(count=0).delete()
        return redirect('cartv')
