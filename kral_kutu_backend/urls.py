"""kral_kutu_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from kral_kutu_backend.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = i18n_patterns(
        path('admin/', admin.site.urls),
        path('', include('order.urls')),

        prefix_default_language=False
        )

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

admin.site.site_header = "KRAL KUTU Admin"
admin.site.site_title = "KRAL KUTU Admin Portal"
admin.site.index_title = "Welcome to KRAL KUTU Portal"


