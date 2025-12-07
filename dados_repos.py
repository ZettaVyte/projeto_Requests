import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('GITHUB_TOKEN')
user = os.getenv('USER_GITHUB')


class DadosRepositorios:
    """
    Classe para extração de dados dos repositórios do GitHub de uma determinada empresa.

    Métodos:
    - lista_repositorios(): Lista os repositórios públicos da empresa.
    - nomes_repos(): Retorna os nomes dos repositórios.
    - nomes_linguagens(): Retorna as linguagens de programação utilizadas nos repositórios
    - cria_df_linguagens(): Cria um DataFrame com os nomes dos repositórios e suas linguagens.

    Atributos:
    - owner (str): Nome da empresa/dono dos repositórios.
    - api_base_url (str): URL base da API do GitHub.
    - access_token (str): Token de acesso para autenticação na API do GitHub.
    - headers (dict): Cabeçalhos HTTP para as requisições à API do GitHub.
    """

    def __init__(self, owner: str):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = token
        self.headers = {
            'Authorization': f'token {self.access_token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def lista_repositorios(self):
        """
        Lista os repositórios públicos da empresa.

        Returns:
            list: Lista de repositórios públicos.
        """
        repos_list = []

        for page_num in range(1, 20):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers = self.headers)
                repos_list.append(response.json())
            except Exception as e:
                repos_list.append(f'Erro na página {page_num}: {e}')

        return repos_list

    #desafio: otimizando a paginação
    def lista_repositorios2(self):
        """
        Lista os repositórios públicos da empresa de forma mais otimizada.

        Returns:
            list: Lista de repositórios públicos.
        """

        repos_list = []
        url = f'{self.api_base_url}/users/{self.owner}'
        repos_publicas = requests.get(url, headers = self.headers).json()['public_repos']
        for page_num in range(1, repos_publicas // 30 + 2): #cada página tem 30 repositórios e somamos 1 para pegar o resto
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers = self.headers)
                repos_list.append(response.json())
            except Exception as e:
                repos_list.append(f'Erro na página {page_num}: {e}')

        return repos_list


    def nomes_repos(self, repos_list: list):
        """
        Retorna os nomes dos repositórios.

        Args:
            repos_list (list): Lista de repositórios públicos.

        Returns:
            list: Lista de nomes dos repositórios.
        """
        repo_names = []
        for page in repos_list:
            for repo in page:
                if repo['name'] is not None:
                    repo_names.append(repo['name'])


        return repo_names

    def nomes_linguagens(self, repos_list: list):
        """
        Retorna as linguagens de programação utilizadas nos repositórios.

        Args:
            repos_list (list): Lista de repositórios públicos.

        Returns:
            list: Lista de linguagens de programação.
        """

        repo_languages = []
        for page in repos_list:
            for repo in page:
                if repo['language'] is not None:
                    repo_languages.append(repo['language'])

        return repo_languages

    def cria_df_linguagens(self):
        """
        Cria um DataFrame com os nomes dos repositórios e suas linguagens.
        Returns:
            pd.DataFrame: DataFrame com os nomes dos repositórios e suas linguagens.
        """

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame({
            'repository_name': nomes,
            'language': linguagens
        })

        return dados
