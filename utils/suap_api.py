import requests

class Suap:
    def __init__(self,token=False, refresh_token = False, request = None):
        
        if token:
            self.token = token
        if refresh_token:
            self.refresh_token = refresh_token

        self.request = request
        self.token = None
        self.endpoint = 'https://suap.ifrn.edu.br/api/v2/'
        
    def authenticate(self, username, password, setToken=True):
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
                    print('NÃO EXISTE DICT TOKEN')
                    self.setToken(data['access']) 

        return data
    
    def setToken(self, token):
        self.request.session['token'] = 'i can catch that'
        self.request.session['refresh_token'] = 'i can catch that'
        self.token = token

    def refreshToken(self):
        pass
        # FAZER AQUI REQUISIÇÃO PARA ATUALIZAR O TOKEN

    def getUserData(self):
        url = self.endpoint+'minhas-informacoes/meus-dados/'
        response = self.doGETRequest(url)
        
        data = {}
        data.department = response['tipo_vinculo']
        data.registration = response['matricula']
        data.name = response['nome_usual']
        data.picture = response['url_foto_75x100']

        return data

    def doGETRequest(self, url):
        
        response = requests.get(url, headers={'Authorization': f'Bearer {self.token}'})
        if (response.status_code == 401):
            self.refreshToken()
        data = False
        if response.status_code == 200:
            data = response.json()
        return data