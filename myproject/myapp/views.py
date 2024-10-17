from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def admin_view(request):
    return render(request, 'admin.html')

def formulario_retiro(request):
    return render(request, 'formulario-retiro.html')

def retiros_pendientes(request):
    return render(request, 'retiros-pendientes.html')

def test_loading(request):
    return render(request, 'test-loading.html')

def historial_usuario(request):
    return render(request, 'usuario-historial.html')

def boleta(request):
    return render(request, 'boleta.html')