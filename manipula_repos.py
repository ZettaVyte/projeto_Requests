import os
from dotenv import load_dotenv
import requests
import base64
import logging

logging.basicConfig(
    filename='manipula_repos.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

load_dotenv()
token = os.getenv('GITHUB_TOKEN')
user = os.getenv('USER_GITHUB')


class ManipulaRepositorios:
    """
    Classe para manipulação de repositórios do GitHub.]

    Métodos:
    - cria_repo(nome_repo): Cria um novo repositório no GitHub.
    - add_arquivo(nome_repo, nome_arquivo, caminho_arquivo): Adiciona um arquivo a um repositório existente no GitHub.

    """

    def __init__(self, username: str):
        """
        Inicializa a classe com o nome de usuário do GitHub.

        Args:
            username (str): Nome de usuário do GitHub.
        """
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = token
        self.headers = {
            'Authorization': f'token {self.access_token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def cria_repo(self, nome_repo: str):
        """
        Cria um novo repositório no GitHub.

        Args:
            nome_repo (str): Nome do repositório a ser criado.

        Returns:
            None: A função apenas imprime o status da criação do repositório.

        Raises:
            Exception: Se ocorrer um erro durante a criação do repositório.
        """
        data = {
            'name' : nome_repo,
            'description': 'Repositório para armazenar as linguagens de programação das empresas com repositórios públicos no GitHub.',
            'private': False
        }

        try:
            response = requests.post(f'{self.api_base_url}/user/repos', headers=self.headers, json=data)
            logging.info(f'Criação do repositório {nome_repo}: {response.status_code}')
        except Exception as e:
            logging.error(f'Erro ao criar o repositório {nome_repo}: {e}')

    def add_arquivo(self, nome_repo: str, nome_arquivo: str, caminho_arquivo: str):
        """
        Adiciona um arquivo a um repositório existente no GitHub.

        Args:
            nome_repo (str): Nome do repositório.
            nome_arquivo (str): Nome do arquivo a ser adicionado.
            caminho_arquivo (str): Caminho local do arquivo a ser adicionado.
        """
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()
        logging.info(f'Lendo o arquivo {nome_arquivo} do caminho {caminho_arquivo}')
        encoded_content = base64.b64encode(file_content).decode('utf-8')

        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'
        logging.info(f'URL para adicionar o arquivo {nome_arquivo}: {url}')
        data = {
            'message': f'Adicionando o arquivo {nome_arquivo}',
            'content': encoded_content
        }
        try:
            response = requests.put(url, headers=self.headers, json=data)
            logging.info(f'Adição do arquivo {nome_arquivo} ao repositório {nome_repo}: {response.status_code}')
        except Exception as e:
            logging.error(f'Erro ao adicionar o arquivo {nome_arquivo} ao repositório {nome_repo}: {e}')
