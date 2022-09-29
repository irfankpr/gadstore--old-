from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from profiles.models import userprofiles


# Create your views here.


@never_cache
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/')
        return redirect('/home')
    else:
        return redirect('/log')

# signup module
def signin(request):
    if request.method == 'POST':
        if request.POST['Fname'] and request.POST['Sname'] and request.POST['Password1'] and request.POST['Password2'] and request.POST['email'] and request.POST['phone']:
            Fname=request.POST['Fname']
            Sname = request.POST['Sname']
            passw1 = request.POST['Password1']
            passw2 = request.POST['Password2']
            email = request.POST['email']
            phone = request.POST['phone']
            if passw2 == passw1:
                usr = userprofiles.objects.create_user(first_name=Fname,second_name=Sname,password=passw1,email=email,phone=phone)
                usr.save()
                print("user sign inned successfully")
                auth.login(request, usr)
                res = redirect('/home')
                res.set_cookie('username',Fname + Sname)
                res.set_cookie('password', passw1)
                request.session['username'] = Fname + Sname
                request.session['password'] = passw1
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
        if request.POST['phone'] and request.POST['Password'] :
            Phone = request.POST['phone']
            password = request.POST['Password']
            print(Phone,password)
            usr = authenticate(request,username=Phone,password=password)
            if usr is not None:
                auth.login(request,usr)
                res = redirect('/home')
                user = userprofiles.objects.get(phone=Phone)
                res.set_cookie('username', user.first_name + usr.second_name)
                res.set_cookie('password', password)
                request.session['username'] = user.first_name + usr.second_name
                request.session['password'] = password
                return res

            else:
                messages.error(request,'Invalid credentials.')
                return redirect('/log')
        else:
            messages.error(request, 'you cannot submit without credentials filled !')
            return redirect('/log')
    else:
        return redirect('/log')




@never_cache
def sign(request):
    return render(request, 'User-Signin.html')

@never_cache
def log(request):
    return render(request, 'User-Login.html')

@never_cache
def home(request):
    return render(request, 'index.html')

@never_cache
def products(request):
    return render(request, 'shop.html')

@never_cache
def cart(request):
    return render(request, 'cart.html')

@never_cache
def dtl(request):
    return render(request, 'detail.html')

@never_cache
def chkout(request):
    return render(request, 'checkout.html')
