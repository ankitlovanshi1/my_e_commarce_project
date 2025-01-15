from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    # Fetch all products from the database
    products = Product.objects.all()
    # Pass the products to the template
    return render(request, 'home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

