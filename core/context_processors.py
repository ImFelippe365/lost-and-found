from .models import Administrator
from django.http import HttpResponseRedirect
from django.urls import reverse
from utils import suap_api

def onLogout(request, id):
    token = request.session['token', None]
    refresh_token = request.session['refresh_token', None]
    user = request.session['user', None]
    

    return HttpResponseRedirect(reverse('index'))

def isAuthenticated(request):
    print('CONTEXT PROCESSORS -> FUI REQUISITADO NOVAMENTE')
    
    token = request.session.get('token')
    refresh_token = request.session.get('refresh_token')
    user = request.session.get('user')

    auth = None
    if (token is not None):
        auth = suap_api.Suap(token, refresh_token, request)

    if (user is not None):
        return { 'is_authenticated': True, 'user': user, 'logout': onLogout }
    elif (user is None and token is not None):
        user = auth.getMeusDados()
        return { 'is_authenticated': True, 'user': user, 'logout': onLogout }
    else:
        return { 'is_authenticated': False }