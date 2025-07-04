from django.shortcuts import render
from .models import Product

def index(request):
    return render(request, 'swapandsell/index.html')


def all_gadgets(request):
    all_gadgets = Product.objects.order_by('-listing_date')
    context = {'all_gadgets': all_gadgets}
    return render(request, 'swapandsell/all_gadgets.html', context)
# Create your views here.
