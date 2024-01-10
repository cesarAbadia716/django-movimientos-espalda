from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitoreo_espalda/', include('monitoreo_espalda.urls')),
]
