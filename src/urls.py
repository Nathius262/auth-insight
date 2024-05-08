from django.contrib import admin
from django.urls import path, include
from authentication.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('', index_view, name='index')
]
