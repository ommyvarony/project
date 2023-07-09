from django.contrib import admin
from .models import products
from .models import cart
# Register your models here.


admin.site.register(products)
admin.site.register(cart)