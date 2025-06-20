from django.urls import path
from .views import registrar_plantao

urlpatterns = [
    path('', registrar_plantao, name='registrar_plantao'),
]
