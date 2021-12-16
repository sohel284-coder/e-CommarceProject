from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView

from app_shop.models import *




def home(request, ):
    products = Product.objects.filter()
    return render(request, 'shop_app/home.html', {
        'products':products,
    })    
    
@login_required(login_url='/account/login/')
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop_app/product_detail.html', {
        'product':product,
    })

def search_product(request):
    search_peram = request.GET.get('search')
    print(search_peram)
    if search_peram:
        products = Product.objects.filter(name__icontains=search_peram)
    return render(request, 'shop_app/search_product.html', {
        'search':search_peram,
        'products':products,
    })

