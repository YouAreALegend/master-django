from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^master-django/admin/', admin.site.urls),
    url(r'^master-django/',include('front.urls')),
]
