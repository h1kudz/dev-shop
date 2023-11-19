from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'new_price',
                    'is_available', 'pub_date', 'updated']
    list_filter = ['is_available', 'pub_date', 'updated']
    list_editable = ['new_price', 'is_available']
    search_fields = ['name', 'category', 'description']
    prepopulated_fields = {'slug': ('name',)}

    def short_queryset(self, obj):
        if len(obj.description) > 100:
            return obj.description[:100] + '...'
        else:
            return obj.description