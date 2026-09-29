from django.urls import path
from .views.views import LeyEnfriamientoView

app_name = "ley_enfriamiento"

urlpatterns = [
    path("", LeyEnfriamientoView.as_view(), name="ley-enfriamiento"),
    path("calcular/", LeyEnfriamientoView.as_view(), name="ley-enfriamiento-calcular"),
]
