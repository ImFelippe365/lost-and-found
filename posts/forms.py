from django import forms
from .models import Item


class ItemModelForm(forms.Form):
    class Meta:
        model = Item
        fields = ['who_found', 'local_found', 'when_was_found', 'shift',
                   'name', 'image', 'description',
                   'pickup_location', 'withdrawal_deadline']