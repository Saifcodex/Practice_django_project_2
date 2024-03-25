from django.shortcuts import render
from products.models import Product


def home(request):
    return render(request, 'home.html')


def product_page(request):
    product = Product.objects.all()
    return render(request, 'productpage.html', {
        'product': product,
    })


