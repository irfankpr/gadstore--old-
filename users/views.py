from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import auth
from profiles.models import userprofiles, cart
from OTP.views import otpgen
from products.models import categories, products, sub_categories


# Create your views here.


@never_cache
def index(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin')
        else:
            return redirect('/home')
    else:
        return redirect('landing')


# signup module
def signin(request):
    if request.method == 'POST':
        if request.POST['Fname'] and request.POST['Sname'] and request.POST['Password1'] and request.POST[
            'Password2'] and request.POST['email'] and request.POST['phone']:
            Fname = request.POST['Fname']
            Sname = request.POST['Sname']
            passw1 = request.POST['Password1']
            passw2 = request.POST['Password2']
            email = request.POST['email']
            phone = request.POST['phone']
            if userprofiles.objects.filter(phone=phone).exists():
                messages.error(request, 'Phone already exist')
                return redirect('/sign')
            if userprofiles.objects.filter(email=email).exists():
                messages.error(request, 'e-mail already exist')
                return redirect('/sign')
            if passw2 == passw1:
                usr = userprofiles.objects.create_user(first_name=Fname, last_name=Sname, password=passw1, email=email,
                                                       phone=phone)
                usr.save()
                print("user sign inned successfully")
                auth.login(request, usr)
                res = redirect('/home')
                res.set_cookie('user_id', usr.id)
                return res
            else:
                print("password confirmation failed")
                messages.error(request, 'Password confirmation failed ')
                return redirect('/sign')
        else:
            messages.error(request, 'you cannot submit without credentials filled !')
            return redirect('/sign')
    else:
        return redirect('/sign')


def login(request):
    if request.method == 'POST':
        if request.POST['phone'] and request.POST['Password']:
            Phone = request.POST['phone']
            password = request.POST['Password']
            usr = authenticate(request, phone=Phone, password=password)
            user = userprofiles.objects.get(phone=Phone)
            if usr is not None:
                if user.blocked:
                    messages.error(request, 'You are restricted by admin')
                    return redirect('/log')
                auth.login(request, user)
                res = redirect('/home')
                user = userprofiles.objects.get(phone=Phone)
                res.set_cookie('user_id', user.id)
                return res

            else:
                messages.error(request, 'Invalid credentials.')
                return redirect('/log')
        else:
            messages.error(request, 'you cannot submit without credentials filled !')
            return redirect('/log')
    else:
        return redirect('/log')


def loginotp(request):
    if request.method == "GET" and request.GET['phone']:
        phone = request.GET['phone']
        otpgen.send_otp(phone)
        messages.error(request, 'OTP sent to ' + phone)
        return redirect('/otp')


def usr_logout(request):
    logout(request)
    return redirect('/')


@never_cache
def sign(request):
    return render(request, 'User-Signin.html')


@never_cache
def log(request):
    return render(request, 'User-Login.html')


@login_required(login_url='/')
@never_cache
def home(request):
    if request.user.is_authenticated:
        count = cart.objects.filter(user_id=request.user.id).count()
        new = products.objects.all().order_by('-added_date')[:8]
        cat = categories.objects.all().annotate(cat_count=Count('category_name')).order_by('category_name')
        subcat = sub_categories.objects.all().annotate(subcat_count=Count('sub_cat_name')).order_by('sub_cat_name')
        return render(request, 'index.html', {'cat': cat, 'new': new, 'subcat': subcat, 'count': count})
    else:
        messages.error(request, 'Something went wrong, please try again')
        return redirect('/log')


@never_cache
def shop(request):
    if request.method == 'GET':
        if request.GET['key']:
            key = request.GET['key']
            q = Q()
            q &= Q(Product_name__icontains=key) | Q(products_desc__icontains=key)
            prds = products.objects.filter(q)
            print(key, "................................")
            count = cart.objects.filter(user_id=request.user.id).count()
            cat = categories.objects.all().annotate(cat_count=Count('category_name')).order_by('category_name')
            subcat = sub_categories.objects.all().annotate(subcat_count=Count('sub_cat_name')).order_by('sub_cat_name')
            return render(request, 'shop.html',
                          {'products': prds, 'key': key, 'cat': cat, 'subcat': subcat, 'count': count})


        else:
            count = cart.objects.filter(user_id=request.user.id).count()
            cat = categories.objects.all().annotate(cat_count=Count('category_name')).order_by('category_name')
            subcat = sub_categories.objects.all().annotate(subcat_count=Count('sub_cat_name')).order_by('sub_cat_name')
            prds = products.objects.filter()
            return render(request, 'shop.html',
                          {'products': prds, 'key': 'Search products', 'cat': cat, 'subcat': subcat, 'count': count})


@never_cache
def cartv(request):
    crt = cart.objects.filter(user_id=request.user.id).order_by('product_id')
    prd = products.objects.filter()
    return render(request, 'cart.html', {'cart': crt, 'product': prd})



@never_cache
def dtl(request, id):
    count = cart.objects.filter(user_id=request.user.id).count()
    prd = products.objects.filter(id=id)
    d = products.objects.get(id=id)
    like = products.objects.filter(category_id=d.category_id)
    return render(request, 'detail.html', {'product': prd, 'count': count,'Like':like})


@login_required(login_url='/')
@never_cache
def chkout(request):
    return render(request, 'checkout.html')


@never_cache
def landing(request):
    count = cart.objects.filter(user_id=request.user.id).count()
    new = products.objects.all().order_by('-added_date')[:8]
    cat = categories.objects.all().annotate(cat_count=Count('category_name')).order_by('category_name')
    subcat = sub_categories.objects.all().annotate(subcat_count=Count('sub_cat_name')).order_by('sub_cat_name')
    return render(request, 'gadstore.html', {'cat': cat, 'new': new, 'subcat': subcat, 'count': count})


@never_cache
@login_required(login_url='/')
def checkout(request):
    return render(request, 'checkout.html')
