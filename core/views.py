from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from .models import Administrator
from utils import suap_api

def index(request):
    return render(request, 'index.html')

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            suap = suap_api.Suap()
            isAuthenticated = suap.autenticar(username, password)
            print("isAuthenticated ->", isAuthenticated)
            if not (isAuthenticated):
                form.add_error("username","Usuário e/ou senha incorreto(s). Tente novamente")
                return render(request, 'login.html', {'form': form})
            else:
                dados = suap.getMeusDados()
                print("Dados que peguei ->", dados)
                newAuth = Administrator()
                newAuth.department = dados['tipo_vinculo']
                newAuth.registration = dados['matricula']
                newAuth.name = dados['nome_usual']
                newAuth.picture = dados['url_foto_75x100']
                newAuth.save()
                print(newAuth)
                return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})