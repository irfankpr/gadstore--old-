from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.text import slugify

from products.models import categories


# Create your views here.
def addcat(request):
    if request.method == 'POST':
        if request.POST['catname'] and request.POST['Description'] and request.FILES['catimage']:
            name = request.POST['catname']
            des = request.POST['Description']
            obj = categories()
            obj.category_name = name
            obj.description = des
            obj.slug = slugify(name)
            obj.category_image = request.FILES['catimage']
            obj.save()
            messages.error(request, 'New category added')
            return redirect('category')

        else:
            messages.error(request, 'fill all fields')
            return redirect('category')


def deletecat(request, catid):
    id = catid
    categories.objects.filter(id=id).delete()
    return redirect('/adminhome')
