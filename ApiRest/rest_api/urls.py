from django.urls import path
from rest_api.views import lista_usuarios,login_usuario

urlpatterns = [
    path('lista_usuarios', lista_usuarios, name='Lista Usuarios'),
    path('login_usuario', login_usuario, name='Login Usuario' ),
]
