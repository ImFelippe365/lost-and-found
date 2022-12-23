from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
import requests
from .models import Administrator

class Suap:
    def __init__(self,token=False):
        
        if token:
            self.token = token
        self.token = None

        self.endpoint = 'https://suap.ifrn.edu.br/api/v2/'
        
    def autenticar(self, username, password, setToken=True):

        url = self.endpoint+'autenticacao/token/'
        params = {
            'username':username,
            'password':password,
        }

        response = requests.post(url, data=params)
        data = False

        print("RESPOSTA AO AUTENTICAR -> ",response.json())
        if response.status_code == 200:
            data = response.json()
            if setToken:
                try:
                    self.setToken(data['token'])  
                except:
                    self.setToken(data['access']) 

        return data
    
    def setToken(self, token):
        self.token = token

    def getMeusDados(self):
        url = self.endpoint+'minhas-informacoes/meus-dados/'
        return self.doGETRequest(url)

    def doGETRequest(self, url):
        response = requests.get(url, headers={'Authorization': f'Bearer {self.token}'})
        data = False
        if response.status_code == 200:
            data = response.json()
        return data

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

            suap = Suap()
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