from django.contrib import admin

from order.models import Leather, LeatherSerial, Order, Product, ProductCategory


@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    list_display = (
    'upper_case_name', 'phone', 'address', 'date_last_updated', 'deleted')
    list_display_links = ('upper_case_name',)
    list_editable = ('deleted',)
    list_filter = ('deleted',)
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'address',)
    date_hierarchy = 'date_created'
    ordering = ('date_created', 'date_last_updated')

    @staticmethod
    def upper_case_name(obj):
        return ("%s %s" % (obj.first_name, obj.last_name)).title()

    upper_case_name.short_description = 'Name'


@admin.register(LeatherSerial)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'deleted')
    list_display_links = ('name',)
    list_editable = ('deleted',)
    list_filter = ('deleted',)
    search_fields = ('name',)


@admin.register(Leather)
class PostAdmin(admin.ModelAdmin):
    list_display = ('code', 'serial', 'image', 'deleted',)
    list_display_links = ('code',)
    list_editable = ('image', 'deleted')
    list_filter = ('serial', 'deleted',)
    search_fields = ('code',)


@admin.register(ProductCategory)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'deleted',)
    list_display_links = ('name',)
    list_editable = ('deleted',)
    list_filter = ('deleted',)
    search_fields = ('name',)


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'category', 'price', 'deleted',)
    list_editable = ('image', 'category', 'price', 'deleted',)
    list_display_links = ('id',)
    list_filter = ('category', 'deleted',)
    search_fields = ('deleted',)
