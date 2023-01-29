from django.http import HttpResponseRedirect
from django.urls import reverse
from utils import suap_api

def onLogout(request):
    request.session.pop('token')
    request.session.pop('refresh_token')
    request.session.pop('user')
    
    return HttpResponseRedirect(reverse('index'))

def isAuthenticated(request):
    token = request.session.get('token')
    refresh_token = request.session.get('refresh_token')
    user = request.session.get('user')
    auth = None

    if (token is not None):
        auth = suap_api.Suap(token, refresh_token)

    if (user is not None):
        return { 'is_authenticated': True, 'user': user, 'logout': onLogout }
    elif (user is None and token is not None):
        user = auth.getUserData(token)
        user.pop('success')
        request.session['user'] = user
        return { 'is_authenticated': True, 'user': user, 'logout': onLogout }
    
    return { 'is_authenticated': False }