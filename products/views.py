from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request,
            'product/index.html',
            {'category': category,
             'categories': categories,
             'products': products})

def show(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                is_available=True)
    
    cart_product_form = CartAddProductForm()
    return render(request,
                    'product/show.html',
                     {'product': product, 
                     'cart_product_form': cart_product_form})


