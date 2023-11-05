from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ("category_name", "category_slug",)
    prepopulated_fields = {"category_slug" : ("category_name",)}
    

admin.site.register(Category, CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_category', 'stock_quantity', 'stock_unit', 'modified_date', 'created_date',  'is_available',)
    list_filter = ('product_category', 'is_available')
    list_editable = ("is_available",)
    prepopulated_fields = {"product_slug": ("product_name",)}
admin.site.register(Product, ProductAdmin)