from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, redirect, render


from store.models import Product,Cart,Order

# Create your views here.

def Getdata_indexStore(request):
    products = Product.objects.all()
    html = render_to_string('product_list.html', {'products': products})
    return JsonResponse({'html': html})

def Viewdata_indexStore(request):
    return render(request, 'index_store.html')

def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request,'detail.html', context={"product": product})


def add_to_cart(request,slug):
    
   
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        user = request.user
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
    
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        cart = get_object_or_404(Cart, user=request.user)
        return render(request,'cart.html', context={"orders": cart.orders.all()})



def delete_article(request, order_id):
   
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        order = get_object_or_404(Order, id=order_id, user=request.user)
        order.delete()
        return redirect('cart')

