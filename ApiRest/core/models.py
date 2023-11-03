from django.db import models

# Create your models here.

class User(models.Model):
  id = models.AutoField(primary_key=True)
  usuario = models.CharField(max_length=100, unique=True)
  contraseña = models.CharField(max_length=100)
  apaterno = models.CharField(max_length=30)
  pnombre = models.CharField(max_length=30)

  def __str__(self):
        return str(self.usuario)

class TipoUser(models.Model):
  id_tipo = models.AutoField(primary_key=True, db_column='id_tipo')
  tipo_usuario = models.CharField(max_length= 100) 

  def __str__(self):
        return str(self.tipo_usuario)
