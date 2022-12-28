from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from utils import suap_api

def index(request):
    return render(request, 'index.html')

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            suap = suap_api.Suap()
            isAuthenticated = suap.authenticate(username, password)

            if not (isAuthenticated):
                form.add_error("username","Usuário e/ou senha incorreto(s). Tente novamente")
                return render(request, 'login.html', {'form': form})
            else:
                request.session['token'] = isAuthenticated['access']
                request.session['refresh_token'] = isAuthenticated['refresh']
                return HttpResponseRedirect('items/')
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })