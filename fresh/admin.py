from django.contrib import admin
from .models import Vegies
from .models import Product 
from .models import Cart
from .models import CartItem


# Register your models here.


admin.site.register(Vegies)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
