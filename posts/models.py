from django.db import models



class Item(models.Model):
    status = models.CharField(verbose_name='Status', max_length=8)
    name = models.CharField(verbose_name='Nome *', max_length=20)
    description = models.CharField(verbose_name='Descrição', max_length=150)
    who_found = models.CharField(verbose_name='Nome de quem encontrou *', max_length=50)
    local_found = models.CharField(verbose_name='Local que foi encontrado *', max_length=20)
    when_was_found = models.DateField(verbose_name='Data de quando foi encontrado *')
    image = models.ImageField(verbose_name='Foto', null=True, blank=True)
    shift = models.CharField(verbose_name='Turno', max_length=8)
    withdrawal_deadline = models.DateField(verbose_name='Data limite para retirada *')
    pickup_location = models.CharField(verbose_name='COADES *', max_length=20)
    