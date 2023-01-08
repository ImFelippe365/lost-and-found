import requests

class Suap:
    def __init__(self,token=False, refresh_token = False):
        if token:
            self.token = token
        if refresh_token:
            self.refresh_token = refresh_token
        
        self.token = None
        self.endpoint = 'https://suap.ifrn.edu.br/api/v2/'
        
    def authenticate(self, username, password):
        url = self.endpoint+'autenticacao/token/'
        params = {
            'username': username,
            'password': password,
        }

        response = requests.post(url, data=params)
        data = False

        if response.status_code == 200:
            data = response.json()
            self.setToken(data['access']) 
            self.setRefreshToken(data['refresh'])
            print(data['access'])
        else:
            print('(!) Não foi possível logar, erro: ', response)
        return data
    
    def setToken(self, token):
        self.token = token

    def setRefreshToken(self, refresh_token):
        self.refresh_token = refresh_token

    def refreshToken(self):
        url = self.endpoint+'autenticacao/token/refresh/'
        params = {
            'refresh': self.refresh_token
        }
        response = requests.post(url, data=params)
        if response.status_code == 200:
            data = response.json()
            self.setToken(data)
            print("REFRESH TOKEN",data)
        else:
            print("(!) Não foi possível atualizar o token", response.status_code)

    def getUserData(self, token):
        url = self.endpoint+'minhas-informacoes/meus-dados/'
        response = self.doGETRequest(url, token)
        data = {
            'name': response['nome_usual'],
            'picture': response['url_foto_75x100'],
            'department': response['tipo_vinculo'],
            'registration': response['matricula'],
        }

        return data

    def doGETRequest(self, url, token):
        response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
        data = False
        if response.status_code == 200:
            data = response.json()
        return data