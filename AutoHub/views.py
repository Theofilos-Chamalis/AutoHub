from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from AutoHub.models import Car
from AutoHub.models import Seller
from AutoHub.models import Manufacturer
from django.db.models import Q


def home_page(request):
    return render(request, 'home_page.html')


def car_list(request):
    cat = request.GET.get('cat', '')
    txt = request.GET.get('txt', '')
    try:
        cat = int(cat)
    except:
        cat = False
    if cat is False:
        if txt == '':
            cars = Car.objects.order_by('title')
        else:
            cars = Car.objects.filter((Q(text__contains=txt) | Q(title__contains=txt)) & Q(published_date__lte=timezone.now())).order_by('title')
    else:

        cars = Car.objects.filter(Fuel=cat).order_by('title')
    return render(request, 'car_list.html', {'cars': cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_detail.html', {'car': car})


def seller_list(request):
    txt = request.GET.get('txt', '')
    if txt == '':
        sellers = Seller.objects.order_by('last_name')
    else:
        sellers = Seller.objects.filter(last_name__contains=txt).order_by('last_name')
    return render(request, 'seller_list.html', {'sellers': sellers})


def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    return render(request, 'seller_detail.html', {'seller': seller})


def manufacturer_list(request):
    cat1 = request.GET.get('cat1', '')
    txt = request.GET.get('txt', '')
    try:
        cat1 = int(cat1)
    except:
        cat1 = False
    if cat1 is False:
        if txt == '':
            manufacturers = Manufacturer.objects.order_by('brand')
        else:
            manufacturers = Manufacturer.objects.filter(Q(brand__contains=txt)).order_by('brand')
    else:
        manufacturers = Manufacturer.objects.filter(country=cat1).order_by('brand')

    return render(request, 'manufacturer_list.html', {'manufacturers': manufacturers})


def manufacturer_detail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    return render(request, 'manufacturer_detail.html', {'manufacturer': manufacturer})
