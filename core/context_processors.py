from django.http import HttpResponseRedirect
from django.urls import reverse

def onLogout(request):
    # request.session.pop('token')
    # request.session.pop('refresh_token')
    request.session.pop('user')
    
    return HttpResponseRedirect(reverse('index'))

def isAuthenticated(request):
    # token = request.session.get('token')
    # refresh_token = request.session.get('refresh_token')
    user = request.session.get('user')
    auth = None

    if (user is not None):
        return { 'is_authenticated': True, 'user': user, 'logout': onLogout }
    
    return { 'is_authenticated': False }