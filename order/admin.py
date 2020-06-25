from django.contrib import admin

from order.models import Leather, LeatherSerial, Order, OrderUnit, Product, ProductCategory


@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name',
                    'phone',
                    'address',
                    'date_last_updated',
                    'is_confirmed',
                    'deleted',)

    list_display_links = ('upper_case_name',)

    list_editable = ('is_confirmed',
                     'deleted')

    list_filter = ('is_confirmed',
                   'deleted')

    search_fields = ('first_name',
                     'last_name',
                     'phone',
                     'email',
                     'address',)

    date_hierarchy = 'date_created'

    ordering = ('date_created', 'date_last_updated')

    def upper_case_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name)).capitalize()

    upper_case_name.short_description = 'Name'


@admin.register(OrderUnit)
class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__',
                    'quantity',
                    'inner_leather',
                    'outer_leather',
                    'height',
                    'width',
                    'length',)

    list_display_links = ('__str__',)

    search_fields = ('order',
                     'product',
                     'inner_leather',
                     'outer_leather',
                     'height',
                     'width',
                     'length',)

    list_editable = ('inner_leather',
                     'outer_leather',
                     'height',
                     'width',
                     'length',
                     'quantity',)


@admin.register(LeatherSerial)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'deleted',)

    list_display_links = ('name',)

    list_editable = ('deleted',)

    list_filter = ('deleted',)

    search_fields = ('name',)


@admin.register(Leather)
class PostAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'serial',
                    'image',
                    'deleted',)

    list_display_links = ('code',)

    list_editable = ('image',
                     'deleted')

    list_filter = ('serial',
                   'deleted',)

    search_fields = ('code',)


@admin.register(ProductCategory)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'deleted',)

    list_display_links = ('name',)

    list_editable = ('deleted',)

    list_filter = ('deleted',)

    search_fields = ('name',)


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'title',
                    'image',
                    'category',
                    'inner_leather',
                    'outer_leather',
                    'price',
                    'height',
                    'width',
                    'length',
                    'deleted',)

    list_display_links = ('code',
                          'title',)

    list_editable = ('image',
                     'category',
                     'inner_leather',
                     'outer_leather',
                     'price',
                     'height',
                     'width',
                     'length',
                     'deleted',)

    list_filter = ('category',
                   'deleted',)

    search_fields = ('code',
                     'inner_leather',
                     'outer_leather',
                     'deleted',)
