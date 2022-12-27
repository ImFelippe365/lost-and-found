from .models import Administrator
from django.http import HttpResponseRedirect
from django.urls import reverse

def onLogout(request, id):
    print(id)
    user = Administrator.objects.filter(registration=id)
    print("ESSE É O USER ->",user)
    user.delete()

    return HttpResponseRedirect(reverse('index'))

def isAuthenticated(request):
    user = Administrator.objects.all().first()
    print("TEM USUÁRIO? ->", user)
    if (user is not None):
        return { 'is_authenticated': True, 'user': user, 'logout': onLogout }
    else:
        return { 'is_authenticated': False }

    