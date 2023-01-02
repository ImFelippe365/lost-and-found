from django.db import models
import datetime

class Item(models.Model):

    SHIFT_CHOICES = (
        ('', 'Selecione o turno'),
        ('Morning', 'Manhã'),
        ('Afternoon', 'Tarde'),
        ('Night', 'Noite')
    )
    
    STATUS_CHOICES = (
        ('Lost', 'Perdido'),
        ('Delivered', 'Entregue'),
        ('Expired', 'Expirado')
    )

    PICKUP_LOCATION_CHOICES = (
        ('Bloco Principal', 'Bloco Principal'),
        ('Bloco Anexo', 'Bloco Anexo'),
    )
    
    status = models.CharField(verbose_name='Status', max_length=9, default='Lost')
    name = models.CharField(verbose_name='Nome *', max_length=20)
    description = models.CharField(verbose_name='Descrição', max_length=150)
    who_found = models.CharField(verbose_name='Nome de quem encontrou *', max_length=50)
    local_found = models.CharField(verbose_name='Local que foi encontrado *', max_length=20)
    when_was_found = models.DateField(verbose_name='Data de quando foi encontrado *')
    image = models.ImageField(verbose_name='Foto', null=True, blank=True, upload_to='items')
    shift = models.CharField(verbose_name='Turno', max_length=9, choices=SHIFT_CHOICES)
    withdrawal_deadline = models.DateField(verbose_name='Data limite para retirada *')
    pickup_location = models.CharField(verbose_name='COADES *', max_length=20, choices=PICKUP_LOCATION_CHOICES)
    user_registration = models.CharField(blank=True, max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return self.name


class DeliveredItem(models.Model):
    claimant_name = models.CharField(verbose_name='Nome de quem reivindicou *', max_length=50)
    cpf = models.CharField(verbose_name='CPF', max_length=14)
    withdrawal_date = models.DateTimeField(verbose_name='Data de retirada')