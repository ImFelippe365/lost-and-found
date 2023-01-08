from django.shortcuts import render
from .forms import LoginForm, ErrorList
from django.http import HttpResponseRedirect
from utils import suap_api
from django.template import RequestContext


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
                error = "Usuário e/ou senha incorreto(s). Tente novamente"
                form.add_error("password","Usuário e/ou senha incorreto(s). Tente novamente")
                return render(request, 'login.html', {'form': form, 'error': error})
            else:
                request.session['token'] = isAuthenticated['access']
                request.session['refresh_token'] = isAuthenticated['refresh']
                return HttpResponseRedirect('items/')
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })

def page_not_found(request, exception = None):
    response = render(request, 'page_not_found.html')

    response.status_code = 404
    return response