from django import forms
from django.forms import TextInput
from .models import Item, DeliveredItem, Claimant


class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['who_found', 'when_was_found', 'local_found',  'shift',
                  'name', 'image', 'description',
                  'pickup_location', 'withdrawal_deadline']

        widgets = {
            'who_found': forms.TextInput(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'placeholder': 'Ex: João Silva'
            }),
            'when_was_found': forms.DateInput(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'type': 'date',
            }),
            'local_found': forms.TextInput(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'placeholder': 'Ex: Ginásio'
            }),
            'shift': forms.Select(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'placeholder': 'Selecione o turno',
            }),
            'name': forms.TextInput(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'placeholder': 'Ex: Garrafa'
            }),
            'description': forms.Textarea(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'placeholder': 'Ex: Garrafa de plástico vermelha'
            }),
            'image': forms.FileInput(attrs={
                'class': "hidden",
            }),
            'pickup_location': forms.Select(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'placeholder': 'Selecione o local'
            }),
            'withdrawal_deadline': forms.DateInput(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'type': 'date',
            }),
        }


class CompleteDeliveryModelForm(forms.ModelForm):
    class Meta:
        model = Claimant
        fields = ['name', 'cpf',]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'placeholder': 'Ex: Jorge Silva'
            }),
            'cpf': forms.TextInput(attrs={
                'class': "text-gray border-light-gray rounded-lg px-4",
                'placeholder': 'Insira apenas números',
                'pattern': '[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'
            }),
        }
