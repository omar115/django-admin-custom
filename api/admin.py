'''
notes: in admin py we can customize different things
to view our product. examples:
1. we can make extra column of products to edit directly
2. we can set pagination
3. we can update data directly without going to product

'''


from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status']
    list_editable = ['price']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 20:
            return 'Low'
        return 'High'


# admin.site.register(Product)

