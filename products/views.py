from django.contrib import messages
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.decorators.cache import never_cache
from profiles.models import cart, userprofiles
from products.models import categories, sub_categories, products


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
        if sub_categories.objects.filter(sub_cat_name=subcat):
            messages.error(request, 'Sub category ' + subcat + " alredy exists.")
            return redirect('category')

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



def add_cart(request):
    id = request.GET['proid']

    if cart.objects.filter(user_id_id=request.user.id, product_id_id=id).exists():
        print('exists ......................................................................')
        return JsonResponse({'added': False})
    obj = cart()
    obj.user_id = userprofiles.objects.get(id=request.user.id)
    obj.product_id = products.objects.get(id=id)
    pr = products.objects.get(id=id)
    obj.total = pr.price
    obj.save()
    print('added ......................................................................')
    return  JsonResponse ({'added': True})

def cart_dlt(request, id):
    if request.method == 'GET':
        cart.objects.get(id=id).delete()
        return redirect('cartv')


def cart_count(request):
    if request.method == 'GET':
        c = request.GET['count']
        id = request.GET['cart']
        cart.objects.filter(id=id).update(count=F('count') + c)
        item = cart.objects.get(id=id)
        pr = products.objects.get(id=item.product_id_id)
        cart.objects.filter(id=id).update(total=F('total') + pr.price)
        if cart.objects.filter(count=0):
            cart.objects.filter(count=0).delete()
            return JsonResponse({'removeProduct': True})
        else:
            return JsonResponse({'price': pr.price})
