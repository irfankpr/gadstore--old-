from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import auth
from profiles.models import userprofiles
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
            usr = authenticate(request, phone=Phone, password=password, is_staff=True)
            if usr is not None:
                auth.login(request, usr)
                res = redirect('adminhome')
                user = userprofiles.objects.get(phone=Phone)
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
            prod.products_desc = request.POST["hilights"]
            prod.products_dyl = request.POST["desc"]
            prod.MRP = request.POST["mrp"]
            prod.price = request.POST["price"]
            prod.thumbnail = request.FILES['thumb']
            prod.available_stock = request.POST["count"]
            print(prod)
            prod.save()
            messages.error(request, 'New product ' + prod.Product_name + ' added.', extra_tags='added.')
            return redirect('adminproducts')


        else:
            messages.error(request, 'you cannot submit without credentials filled !', extra_tags='added.')
            return redirect('adminproducts')


def deleteproduct(request, id):
    if request.method == 'GET':
        pr = products.objects.get(id=id)
        name = pr.Product_name
        pr.delete()
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
        return render(request, 'admin/admin-dashbord.html', {'admins': admins})
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
        p = render(request, 'admin/products.html', {'product': product})
        return p

@login_required(login_url='admin')
@never_cache
def add_newproduct(request):
    return render(request, 'admin/add-product.html')




@login_required(login_url='admin')
@never_cache
def users(request):
    usr = userprofiles.objects.filter()
    return render(request, 'admin/users.html', {'user': usr})




@login_required(login_url='admin')
@never_cache
def block_users(request, bid):
    usr = userprofiles.objects.get(id=bid)
    if usr.blocked:
        usr.blocked = False
    else:
        usr.blocked  = True
    usr.save()
    print(usr.blocked)
    usr = userprofiles.objects.filter()
    return redirect(users)
