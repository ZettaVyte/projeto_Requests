import os
from dotenv import load_dotenv
import requests
import base64

load_dotenv()
token = os.getenv('GITHUB_TOKEN')
user = os.getenv('USER_GITHUB')

class ManipulaRepositorios:
    """
    Classe para manipulação de repositórios do GitHub.
    """
    
    
    def __init__(self, username):
        """Inicializa a classe com o nome de usuário do GitHub."""
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = token
        self.headers = {
            'Authorization': f'token {self.access_token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        
    def cria_repo(self, nome_repo):
        """Cria um novo repositório no GitHub."""
        data = {
            'name' : nome_repo,
            'description': f'Repositório para armazenar as linguagens de programação das empresas com repositórios públicos no GitHub.',
            'private': False
        }
        response = requests.post(f'{self.api_base_url}/user/repos', headers=self.headers, json=data)
        print(f'Criação do repositório {nome_repo}:', response.status_code)
        
    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        """Adiciona um arquivo a um repositório existente no GitHub."""
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()
        
        encoded_content = base64.b64encode(file_content).decode('utf-8')
        
        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'
        
        data = { 
            'message': f'Adicionando o arquivo {nome_arquivo}',
            'content': encoded_content
        }
        
        response = requests.put(url, headers=self.headers, json=data)
        print(f'Adição do arquivo {nome_arquivo} ao repositório {nome_repo}:', response.status_code)