from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from profiles.models import userprofiles
from products.models import categories


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


@never_cache
def log(request):
    return render(request, 'admin/admin-login.html')


@never_cache
def adminhome(request):
    admins = userprofiles.objects.filter(is_staff=True)
    return render(request, 'admin/admin-dashbord.html', {'admins': admins})


@never_cache
def category(request):
    cat = categories.objects.all()
    return render(request, 'admin/Category.html', {'cat': cat})
