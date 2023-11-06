from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "created_at", "visible", )
    prepopulated_fields = {"category_slug": ("category_name",)}
    list_editable = ("visible",)
admin.site.register(BlogCategory, CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    list_display = ("title", "blog_category", "modified_at",  "created_at", "visible", )
    prepopulated_fields = {"blog_slug": ("title",)}
    list_editable = ("visible",)


admin.site.register(Blog, BlogAdmin)