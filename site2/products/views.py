from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import Product


# Create your views here.
def add_product(request):
    if request.method == "POST":
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ADD SUCCESSFUL")
    else:
        form = forms.ProductForm()
        return render(request, 'form.html', {'form': form})


def update_product(request, p_id):
    p = Product.objects.get(pk=p_id)
    if request.method == "POST":
        form = forms.ProductForm(request.POST or None, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponse("Upadate Successfully")
    else:
        form = forms.ProductForm(instance=p)
        return render(request, 'form.html', {'form': form})


def delete_product(request, p_id):
    Product.objects.get(pk=p_id).delete()
    return HttpResponse("Delete Successfully")
