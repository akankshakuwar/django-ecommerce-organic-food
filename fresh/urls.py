from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('products/<int:product_id>/', views.products, name='products'),
    path('cart', views.cart, name='cart'),
    path('base', views.base, name="base"),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('home', views.home, name="home"),
    path('shop', views.shop, name="shop"),
    path('contact', views.contact, name="contact"),
    path('checkout', views.checkout, name="checkout"),
    path('<int:pk>', views.product_d, name="product_d"),
    path('order', views.order, name="order"),
  
   
   
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
