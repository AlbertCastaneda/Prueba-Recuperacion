from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirigir_a_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirigir_a_login),
    path('usuarios/', include('usuarios.urls')),
]
