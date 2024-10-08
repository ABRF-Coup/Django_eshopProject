from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import user_passes_test
from .form import ProductForm

from store.models import Product,Cart,Order

# Create your views here.


def Getdata_indexStore(request):
    products = Product.objects.all()
    html = render_to_string('product_list.html', {'products': products, 'page_type': 'home'} )
    return JsonResponse({'html': html})

def Viewdata_indexStore(request):
    return render(request, 'index_store.html')

def Getdata_user(request):
    if not request.user.is_authenticated:
        return redirect('login') # on ajoute aussi une verif ici
    products = Product.objects.filter(user=request.user)
    html = render_to_string('product_list.html', {'products': products,'page_type': 'personal'})
    return JsonResponse({'html': html})

def Viewdata_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'user_product.html')  
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
    

def user_product(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        user_product_list = Product.objects.filter(user=request.user)
        return render(request,'user_product.html', context={"user_product_list": user_product_list})


def delete_product(request, product_id):
    
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        product = get_object_or_404(Product, id=product_id, user=request.user)
        product.delete()
        return redirect('perso')
    
def afficher_form_user_product(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'user_product_form.html')
    
def add_product(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return redirect('perso')
        else:
            form = ProductForm()
        return render(request, 'user_product_form.html', {'form': form})


def search_view(request):
    query = request.GET.get('q', '')
    page_type = request.GET.get('page_type', 'homepage')
    
    # Filter products based on the search query
    if page_type == 'personal' and request.user.is_authenticated:
        products = Product.objects.filter(name__icontains=query, user=request.user)
    else:
        products = Product.objects.filter(name__icontains=query)
    
    # Render the partial template for the search results
    if products.exists():
        results_html = render_to_string('partial_search_results.html', {
        'products': products,
        'page_type': page_type
    })
    else:
        results_html=""
    
    return JsonResponse({'results_html': results_html})