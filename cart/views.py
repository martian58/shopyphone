from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):

    cart = Cart(request)

    cart_products = cart.get_products
    return render(request, 'cart_summary.html', {'cart_products': cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product)

        cart_quantity = cart.__len__()

        response = JsonResponse({'quantity: ': cart_quantity})
        return response
    else:
        pass


def cart_remove(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.remove(product=product_id)

        response = JsonResponse({'product': product_id})

        return response

def cart_update(request):
    return render(request, 'cart.html', {})