from django.shortcuts import render
from .forms import LoginForm, ErrorList
from django.http import HttpResponseRedirect
from utils import suap_api
from django.template import RequestContext
from posts.models import Item


def index(request):
    lost_items = len(Item.objects.filter(status='Lost'))
    delivered_items = len(Item.objects.filter(status='Delivered'))
    expired_items = len(Item.objects.filter(status='Expired'))
    
    context = {
        'lost_items': lost_items,
        'delivered_items': delivered_items,
        'expired_items': expired_items,
    }

    return render(request, 'index.html', context)

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            suap = suap_api.Suap()
            isAuthenticated = suap.authenticate(username, password)
            if not (isAuthenticated['success']):
                error = "Usuário e/ou senha incorreto(s). Tente novamente" if isAuthenticated['message'] == 'Credenciais inválidas' else isAuthenticated['message']
                form.add_error("password","Usuário e/ou senha incorreto(s). Tente novamente")
                return render(request, 'login.html', {'form': form, 'error': error})
            else:
                isAuthenticated.pop('success')
                request.session['user'] = isAuthenticated
                return HttpResponseRedirect('items')
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })

def page_not_found(request, exception = None):
    response = render(request, 'page_not_found.html')

    response.status_code = 404
    return response