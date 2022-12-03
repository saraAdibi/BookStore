from django.contrib import admin
from .models import products, subcategories, categories

# Register your models here.


@admin.register(categories,subcategories,products)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}
    # fieldsets = [
    #     ('images', {'fields': {'image'}}),
    # ]


#
# class ProductsAdmin(admin.ModelAdmin):
#     fieldsets = [('images', {'fields': {'image'}})]
