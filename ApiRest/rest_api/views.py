from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import User
from .serializers import UserSerializer,TipoUserSerializer
from django.contrib.auth import login, authenticate

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_usuarios(resquest):
  user = User.objects.all()
  serializer = UserSerializer(user, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
  if request.method == 'POST':
        # Obtiene los datos del usuario del cuerpo de la solicitud
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            # Guarda el nuevo usuario en la base de datos
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['POST'])
# def login_usuario(request):
 #   usuario = request.data.get('usuario')
  #  contraseña = request.data.get('contraseña')
   # user = authenticate(username=usuario, password=contraseña)
    #print(usuario, contraseña)
    #print(user)
    #if user is not None:
     #   if user.is_active:
    #        login(request, user)
      #      return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
       # else:
        #    return Response({'error': 'La cuenta de usuario está desactivada'}, status=status.HTTP_400_BAD_REQUEST)
   # else:
     #   return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def login_usuario(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        usuario = serializer.validated_data['usuario']
        contraseña = serializer.validated_data['contraseña']
        user = authenticate(username=usuario, password=contraseña)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'La cuenta de usuario está desactivada'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
            
        