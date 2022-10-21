from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import auth
from orders.models import orders
from profiles.models import userprofiles, cart
from products.models import categories, products, prodtct_image, sub_categories


@never_cache
def index(request):
    if request.user.is_authenticated:
        return redirect('adminhome')
    else:
        return render(request, 'admin/admin-login.html')


def login(request):
    if request.method == 'POST':
        if request.POST['phone'] and request.POST['Password']:
            Phone = request.POST['phone']
            password = request.POST['Password']
            print(Phone, password)
            usr = authenticate(request, email=Phone, password=password, is_staff=True, is_admin=True)
            if usr is not None:
                auth.login(request, usr)
                res = redirect('adminhome')
                user = userprofiles.objects.get(email=Phone)
                res.set_cookie('username', user.first_name + usr.last_name)
                res.set_cookie('password', password)
                request.session['username'] = user.first_name + usr.last_name
                request.session['password'] = password
                print("res")
                return res

            else:
                messages.error(request, 'Invalid credentials.')
                return redirect('/admin')
        else:
            messages.error(request, 'you cannot submit without credentials filled !')
            return redirect('/admin')
    else:
        return redirect('/admin')


def log_out(request):
    logout(request)
    return redirect('admin')


def addproduct(request):
    if request.method == "POST":
        if request.POST['name'] and request.POST['mrp'] and request.POST['hilights'] and request.POST['count'] and \
                request.POST['price'] and request.POST['desc'] and request.FILES['thumb']:
            prod = products()
            prod.Product_name = request.POST["name"]
            prod.slug = slugify(prod.Product_name)
            prod.products_dyl = request.POST["hilights"]
            prod.products_desc = request.POST["desc"]
            prod.MRP = request.POST["mrp"]
            prod.price = request.POST["price"]
            prod.thumbnail = request.FILES['thumb']
            prod.available_stock = request.POST["count"]
            prod.category_id = request.POST["cat"]
            ex = products.objects.filter(Product_name=prod.Product_name).exists()
            if ex:
                messages.error(request, 'Product named :- ' + prod.Product_name + ' already exists.')
                return redirect('addproduct')

            prod.save()
            messages.error(request, 'New product ' + prod.Product_name + ' added.', extra_tags='added.')
            return redirect('addproduct')


        else:
            messages.error(request, 'you cannot submit without credentials filled !', extra_tags='added.')
            return redirect('addproduct')


def product_up(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        pname = request.POST['pname']
        obj = products.objects.get(id=pid)
        thumb = obj.thumbnail
        obj.Product_name = request.POST['pname']
        obj.slug = slugify(pname)
        obj.products_dyl = request.POST['hilights']
        obj.products_desc = request.POST['desc']
        obj.MRP = request.POST['mrp']
        obj.price = request.POST['price']
        obj.category_id = request.POST['cat']
        if 'thumbnail' in request:
            obj.thumbnail = request.FILES['thumbnail']
        else:
            obj.thumbnail = thumb
        obj.save()
        messages.error(request, 'Product updated')
        return redirect('adminproducts')


def deleteproduct(request, id):
    if request.method == 'GET':
        pr = products.objects.get(id=id)
        name = pr.Product_name
        pr.delete()
        cart.objects.filter(product_id=id).delete()
        messages.error(request, 'Product ' + name + ' deleted.', extra_tags='dlt')
        return redirect('adminproducts')


@login_required(login_url='admin')
@never_cache
def product_dtl(request, pid):
    prd = products.objects.filter(id=pid)
    cat = categories.objects.all()
    sub = sub_categories.objects.all()
    return render(request, "admin/product-edit.html", {'prd': prd, 'cat': cat, 'sub': sub})


@login_required(login_url='admin')
@never_cache
def adminhome(request):
    if request.user.is_authenticated:
        admins = userprofiles.objects.filter(is_staff=True)
        p = products.objects.filter(available_stock__lte=10)
        dates = orders.objects.values('date__date').annotate(sales=Count('id')).order_by('date__date')
        returns = orders.objects.values('date__date').annotate(returns= Count('id', filter=Q(status='Canceled'))).order_by(
            'date__date')
        print(returns)

        return render(request, 'admin/admin-dashbord.html',
                      {'admins': admins, 'products': p, 'dates': dates, 'returns': returns})
    else:
        return redirect('admin')


@login_required(login_url='admin')
@never_cache
def category(request):
    cat = categories.objects.all()
    return render(request, 'admin/Category.html', {'cat': cat})


@login_required(login_url='admin')
@never_cache
def adm_products(request):
    if request.method == "GET":
        product = products.objects.filter()
        cat = categories.objects.all()
        p = render(request, 'admin/products.html', {'product': product, 'cat': cat})
        return p


@login_required(login_url='admin')
@never_cache
def add_newproduct(request):
    cat = categories.objects.all()
    return render(request, 'admin/add-product.html', {'cat': cat})


@login_required(login_url='admin')
@never_cache
def users(request):
    usr = userprofiles.objects.exclude(is_admin=True).order_by('id')
    return render(request, 'admin/users.html', {'user': usr})


@login_required(login_url='admin')
@never_cache
def block_users(request, bid):
    usr = userprofiles.objects.get(id=bid)
    if usr.blocked:
        print(bid)
        usr.blocked = False
        usr.save()
    else:
        usr.blocked = True
        usr.save()
    print(usr.blocked)
    return redirect(users)


@login_required(login_url='admin')
@never_cache
def cat_edit(request, cid):
    cat = categories.objects.filter(id=cid)
    sub = sub_categories.objects.filter(parent_cat_id=cid)
    return render(request, 'admin/category-edit.html', {'cat': cat, "sub": sub})


def cat_up(request):
    if request.method == "POST":
        id = request.POST['cid']
        obj = categories.objects.get(id=id)
        obj.category_name = request.POST['cname']
        obj.description = request.POST['desc']
        obj.category_image = request.FILES['catimg']
        messages.error(request, 'Category updated ')
        return redirect('category')


def sub_up(request):
    id = request.POST['sid']
    sub_categories.objects.get(id=id).delete()
    messages.error(request, 'Sub-category deleted')
    return redirect('category')


def order(request):
    ord = orders.objects.all().order_by('-date')
    return render(request, 'admin/orders.html', {'orders': ord})
