from django.db import models



class Item(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key=True, unique=True)
    status = models.CharField(verbose_name='Status', max_length=8)
    name = models.CharField(verbose_name='Nome', max_length=20)
    description = models.CharField(verbose_name='Descrição', max_length=150)
    who_found = models.CharField(verbose_name='Quem encontrou', max_length=50)
    local_found = models.CharField(verbose_name='Local encontrado', max_length=20)
    when_was_found = models.DateField(verbose_name='Data encontrado')
    image = models.ImageField(verbose_name='Foto', null=True)
    shift = models.CharField(verbose_name='Turno', max_length=8)
    withdrawal_deadline = models.DateField(verbose_name='Data limite para retirada')
    pickup_location = models.CharField(verbose_name='Local para retirada', max_length=20)
    