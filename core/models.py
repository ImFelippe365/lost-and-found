from django.db import models

# Create your models here.

class Administrator(models.Model):
    registration = models.CharField(max_length=40) # Matrícula do administrador
    name = models.CharField(max_length=50) # Nome do usuário
    department = models.CharField(max_length=100) # Tipo de vínculo
    picture = models.CharField(max_length=50) # Imagem do usuário