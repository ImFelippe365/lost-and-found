from .models import Administrator

def onLogout(request):
    print("SOCORRO ENTREI AQUI DENTRO")
    user = Administrator.objects.all().first()
    if (user):
        user.delete()

    return { 'is_authenticated': False }

def isAuthenticated(request):
    user = Administrator.objects.all().first()

    if (user is not None):
        return { 'is_authenticated': True, 'user': user[0], 'logout': onLogout }
    else:
        return { 'is_authenticated': False }

