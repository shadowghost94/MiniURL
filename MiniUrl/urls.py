from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mini/', include('mini_url.urls') ),
    path('admin/', admin.site.urls),
]
