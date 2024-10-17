from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la vista 'home'

    path('login/', views.login, name='login'),  

    path('registro/', views.registro, name='registro'),  
    
    path('admin/', views.admin_view, name='admin'),

    path('formulario retiro/', views.formulario_retiro, name='formulario retiro'),

    path('retiros pendientes/', views.retiros_pendientes, name='retiros pendientes'), 

    path('loading/', views.test_loading, name='loading'), 

    path('historial usuario/', views.historial_usuario, name='historial usuario'), 

    path('boleta/', views.boleta, name='boleta'), 

]
