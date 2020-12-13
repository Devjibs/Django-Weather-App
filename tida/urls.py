from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ontime/', include('ontime.urls')),
    path('admin/', admin.site.urls),
]
