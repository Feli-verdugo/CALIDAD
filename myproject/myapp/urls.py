from django.urls import path
from . import views  # Importa las vistas desde tu archivo views.py

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la vista 'home'
]
