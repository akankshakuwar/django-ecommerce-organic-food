
from django.shortcuts import render
from .models import Vegies
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required


def products(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    messages.success(request, 'Item removed from cart')
    return redirect('cart')

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    if created:
        cart.quantity = 1
    else:
        cart.quantity += 1
    cart.save()
    return redirect('addc.html')

@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart': cart})




def index(request):

    vegs = Vegies.objects.all()
    return render(request,"index.html", {'vegs': vegs})


def home(request):
    vegs = Vegies.objects.all()
    return render(request,"index.html", {'vegs': vegs})


def shop(request):

    vegs = Vegies.objects.all()
    return render(request,"shop.html", {'vegs': vegs})

def contact(request):
    return render(request,"contact.html")


def base(request):
    return render(request,"base.html")

def checkout(request):
    return render(request,"checkout.html")


def product_d(request, pk):
    veg = Vegies.objects.get(pk=pk)
    context = {'veg': veg}
    return render(request,"product-detail.html", context)


def order(request):
    return render(request,"po.html")