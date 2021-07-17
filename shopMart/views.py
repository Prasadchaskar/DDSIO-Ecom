from django.shortcuts import render
from . models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})


def Details(request,myid):
    all_products = Product.objects.all()
    products=Product.objects.filter(id=myid)
    return render(request,'productDetails.html',{'products':products[0],'all_products':all_products})
 