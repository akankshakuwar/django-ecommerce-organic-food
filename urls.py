
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('fresh.urls')),
    path('base/', include('fresh.urls')),
    path('home/', include('fresh.urls')),
    path('shop/', include('fresh.urls')),
    path('contact/', include('fresh.urls')),
    path('checkout/', include('fresh.urls')),
    path('product_d/', include('fresh.urls')),
    path('cart/', include('fresh.urls')),
    path('products/', include('fresh.urls')),
    path('add_to_cart/', include('fresh.urls')),
    path('remove_from_cart/', include('fresh.urls')),
    path('order/', include('fresh.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
 
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
