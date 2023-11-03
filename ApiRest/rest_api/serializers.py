from rest_framework import serializers
from core.models import User,TipoUser

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','usuario','contraseña']

class TipoUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoUser
    fields = ['id_tipo','tipo_usuario']    