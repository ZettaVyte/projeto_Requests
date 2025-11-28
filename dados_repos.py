import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('GITHUB_TOKEN')
user = os.getenv('USER_GITHUB')


class DadosRepositorios:
    
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = token
        self.headers = {
            'Authorization': f'token {self.access_token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        
    def lista_repositorios(self):
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
    
    
    def nomes_repos(self, repos_list):
        repo_names = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except:
                    pass
                
        return repo_names
    
    def nomes_linguagens(self, repos_list):
        repo_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass
                
        return repo_languages
    
    def cria_df_linguagens(self):
        
        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)
        
        dados = pd.DataFrame({
            'repository_name': nomes,
            'language': linguagens
        })
        
        return dados