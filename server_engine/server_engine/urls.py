from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('bomonka_forum.urls')),
    path('admin/', admin.site.urls),
]
