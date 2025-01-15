from django.shortcuts import render
from .models import Product

def home(request):
    # Fetch all products from the database
    products = Product.objects.all()
    # Pass the products to the template
    return render(request, 'home.html', {'products': products})
