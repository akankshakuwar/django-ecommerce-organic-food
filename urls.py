"""
URL configuration for organic project.

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