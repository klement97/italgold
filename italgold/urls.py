from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('order.urls')),

    prefix_default_language=False
    )

admin.site.site_header = "ITALGOLD Admin"
admin.site.site_title = "ITALGOLD Admin Portal"
admin.site.index_title = "Welcome to ITALGOLD Portal"
