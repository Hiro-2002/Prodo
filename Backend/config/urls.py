from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prodo.profiles.urls')),
    path('api/', include('prodo.todos.urls')),
]
