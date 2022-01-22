from django.contrib import admin
from product.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','weight','price','created_at','updated_at')
admin.site.register(Product,ProductAdmin)