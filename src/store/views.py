from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


from store.models import Product,Cart,Order

# Create your views here.

def index_store(request):
    products = Product.objects.all()
    return render(request,'index_store.html', context={"products": products})


def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request,'detail.html', context={"product": product})


def add_to_cart(request,slug):
    
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    else:
        product = get_object_or_404(Product, slug=slug)
        cart, _ = Cart.objects.get_or_create(user=user)
        order , created = Order.objects.get_or_create(user=user,ordered=False,product=product)
        if created:
            cart.orders.add(order)
            cart.save()
        else:
            order.quantity += 1
            order.save()
        
        return redirect(reverse("product_detail", kwargs={"slug": slug}))

    
def cart(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    else:
        cart = get_object_or_404(Cart, user=request.user)
        return render(request,'cart.html', context={"orders": cart.orders.all()})



def delete_article(request, order_id):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    else:
        order = get_object_or_404(Order, id=order_id, user=request.user)
        order.delete()
        return redirect('cart')

