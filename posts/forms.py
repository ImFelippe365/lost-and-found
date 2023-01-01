from django import forms
from django.forms import TextInput
from .models import Item


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
            'description': forms.TextInput(attrs={
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
        }