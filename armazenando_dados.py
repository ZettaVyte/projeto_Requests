from manipula_repos import ManipulaRepositorios

#instanciando um objeto
novo_repo = ManipulaRepositorios('zettavyte')

#Criando o repositório no GitHub
nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

#Adicionando os arquivos CSV ao repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')

#Desafio final: faltou extrairmos dados referentes à empresa Apple, que também era uma de nossas demandas. Sendo assim, utilizando as classes criadas até aqui, realize o processo de ETL para extrair os dados das linguagens de programação utilizadas nos repositórios da Apple.
novo_repo.add_arquivo(nome_repo, 'linguagens_apple.csv', 'dados/linguagens_apple.csv')
