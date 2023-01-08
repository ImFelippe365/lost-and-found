from django import forms
from django.forms.utils import ErrorList

class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        
        return '<div class="text-error-color">%s</div>'

class LoginForm(forms.Form):
    username = forms.IntegerField(label="Usuário", widget=forms.NumberInput(attrs={
        'class': 'w-full border-light-gray rounded-lg px-4 placeholder:text-gray mb-3',
        'placeholder': 'Insira sua matrícula',
    })
    )
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'class': 'w-full border-light-gray rounded-lg px-4 placeholder:text-gray mb-2',
        'placeholder': 'Insira sua senha',
    }))