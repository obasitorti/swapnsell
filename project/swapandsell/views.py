from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect

def index(request):
    return render(request, 'swapandsell/index.html')


def all_gadgets(request):
    all_gadgets = Product.objects.order_by('-listing_date')
    context = {'all_gadgets': all_gadgets}
    return render(request, 'swapandsell/all_gadgets.html', context)

def add_product(request):
    if request.method != 'POST':
        form = ProductForm()
    else:
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('swapandsell:all_gadgets')
    context = {'form': form}
    return render(request, 'swapandsell/add_product.html', context)

def detail(request, detail_id):
    gadget = Product.objects.get(id=detail_id)
    context = {'gadget': gadget}
    return render(request, 'swapandsell/detail.html', context)

def my_gadgets(request):
    my_gadgets = Product.objects.order_by('-listing_date')
    context = {'all_gadgets': my_gadgets}
    return render(request, 'swapandsell/mygadgets.html', context)

def edit_product(request, detail_id):
    gadget = Product.objects.get(id=detail_id)
    if request.method != 'POST':
        form = ProductForm(instance=gadget)
    else:
        form = ProductForm(instance=gadget, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('swapandsell:all_gadgets')
    context = {'form': form, 'gadget': gadget}
    return render(request, 'swapandsell/edit_product.html', context)