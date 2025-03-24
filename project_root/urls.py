"""URL configuration."""

from django.contrib import admin
from django.urls import include, path

from core.views import index

urlpatterns = [
    path('', index, name='home'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
