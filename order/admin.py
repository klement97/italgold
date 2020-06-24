from django.contrib import admin

# Register your models here.
from order.models import Order, OrderUnit, LeatherSerial, Leather, ProductCategory, Product


@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone',
        'email',
        'address',
        'is_confirmed',
        'deleted',
        'date_created',
        'date_last_updated',)
    list_filter = ('first_name', 'last_name', 'phone', 'email', 'is_confirmed', 'date_created')
    search_fields = ('first_name', 'last_name', 'phone')
    date_hierarchy = 'date_created'
    ordering = ('date_created', 'date_last_updated')


@admin.register(OrderUnit)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'order', 'product', 'quantity', 'inner_leather', 'outer_leather', 'height', 'width', 'length', 'notes',)
    list_filter = ('order', 'product', 'quantity', 'inner_leather')
    search_fields = ('order', 'quantity')


admin.site.register(LeatherSerial)
admin.site.register(Leather)
admin.site.register(ProductCategory)
admin.site.register(Product)
