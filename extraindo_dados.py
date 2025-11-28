from dados_repos import DadosRepositorios

amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()
#print(ling_mais_usadas_amzn)

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

# Salvando os dados 

ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv', index=False)
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv', index=False)
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv', index=False)

#Desafio final: faltou extrairmos dados referentes à empresa Apple, que também era uma de nossas demandas. Sendo assim, utilizando as classes criadas até aqui, realize o processo de ETL para extrair os dados das linguagens de programação utilizadas nos repositórios da Apple.
apple_rep = DadosRepositorios('apple')
ling_mais_usadas_apple = apple_rep.cria_df_linguagens()
ling_mais_usadas_apple.to_csv('dados/linguagens_apple.csv', index=False)
