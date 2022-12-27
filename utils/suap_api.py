import requests

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