"""
URL configuration for Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from store.views import Getdata_indexStore,Viewdata_indexStore,search_view,Getdata_user,Viewdata_user, product_detail,add_to_cart,cart,delete_article,user_product,delete_product,add_product,afficher_form_user_product
from django.conf.urls.static import static
from Shop import settings
from accounts.views import SignUp,LogOut_user,LogIn_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/<str:slug>/', product_detail, name="product_detail"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('cart/',cart,name="cart"),
    path('delete-article/<int:order_id>/', delete_article, name='delete_article'),
    path('', Viewdata_indexStore,name="page_acceuil_boutique"),
    path('getdata',Getdata_indexStore,name="getdata"),
    path('perso/', Viewdata_user,name="perso"),
    path('getdataU',Getdata_user,name="getdataU"),
    path('signup/',SignUp , name="signup"),
    path('logout/',LogOut_user,name="logout"),
    path('login/',LogIn_user,name="login"),
    path('search/',search_view,name="search"),
    path('delete_product/<int:product_id>/',delete_product,name="delete_product"),
    path('perso/product_form/',afficher_form_user_product,name="form_product"),
    path('perso/add_product/',add_product,name="add_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
