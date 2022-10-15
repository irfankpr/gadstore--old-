from django.contrib.auth.decorators import login_required
from django.db.models import F
import razorpay
from orders.models import orders
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from profiles.models import cart, address


# Create your views here.
@login_required(login_url='/')
@never_cache
def chkout(request):
    items = cart.objects.filter(user_id_id=request.user.id)
    total = 0
    add = address.objects.filter(user_id=request.user.id)
    for i in items:
        total = total + i.total
    return render(request, 'checkout.html', {'items': items, 'ttl': total, 'address': add})


@login_required(login_url='/')
@never_cache
def place_order(request):
    if not 'add_id' in request.POST:
        return JsonResponse({'placed': False})
    if request.POST['paym'] == 'COD':
        citems = cart.objects.filter(user_id_id=request.user.id)
        add_id = request.POST['add_id']
        add = address.objects.get(id=add_id)
        for c in citems:
            orders(user=c.user_id, product=c.product_id, quantity=c.count, address=add, status='placed',
                   Total=c.total, payment='COD').save()
        cart.objects.filter(user_id_id=request.user.id).delete()
        return JsonResponse({'placed': True})
    elif request.POST['paym'] == 'razorpay':
        citems = cart.objects.filter(user_id_id=request.user.id)
        add_id = request.POST['add_id']
        add = address.objects.get(id=add_id)
        print(request.user.id,'......................................................................................')
        for c in citems:
            orders(user=c.user_id, product=c.product_id, quantity=c.count, address=add, status='placed',
                   Total=c.total, payment='Razorpay').save()
        cart.objects.filter(user_id_id=request.user.id).delete()
        return JsonResponse({'placed': True})




@login_required(login_url='/')
def order_up(request):
    if request.method == 'POST':
        stt = request.POST['status']
        ord = request.POST['order']
        print(stt, '........................................', ord)
        o = orders.objects.get(id=ord)
        o.status = stt
        o.save()
        return JsonResponse({'ordered': True})
