from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand
from cart.forms import CreateAddProductForm

# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    brands = Brand.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'brands':brands
    }

    return render(request, 'shop/category.html', context)


def product_details(request, id ,slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CreateAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product_details.html', context)

