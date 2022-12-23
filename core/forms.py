from django import forms

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