from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ley-enfriamiento/', include('local_apps.ley_enfriamiento.urls', namespace='ley_enfriamiento')),
    path('api/enfriamiento/', include('local_apps.ley_enfriamiento.urls')),
]
