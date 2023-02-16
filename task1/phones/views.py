from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    db_phones = Phone.objects.all()
    phones = []
    for phone in db_phones:
        phones.append(phone.__dict__)

    sorting = request.GET.get("sort")
    if sorting == 'min_price':
        phones = sorted(phones,key= lambda d: d['price'])
    elif sorting == 'max_price':
        phones = sorted(phones,key= lambda d: d['price'],reverse=True)
    elif sorting == 'name':
        phones = sorted(phones,key= lambda d: d['name'][0].lower())

    context = {'phones':phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug = slug).__dict__
    context = {'phone':phone}
    return render(request, template, context)
