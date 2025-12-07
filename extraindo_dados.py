from dados_repos import DadosRepositorios

import logging

logging.basicConfig(
    filename='pipeline_dados.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Iniciando o processo de ETL...")

try:
    logging.info("Extraindo dados dos repositórios da Amazon...")
    amazon_rep = DadosRepositorios('amzn')
    ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()
    logging.info("Dados da Amazon extraídos com sucesso: %s linhas.", len(ling_mais_usadas_amzn))

    logging.info("Extraindo dados dos repositórios da Netflix...")
    netflix_rep = DadosRepositorios('netflix')
    ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()
    logging.info("Dados da Netflix extraídos com sucesso: %s linhas.", len(ling_mais_usadas_netflix))

    logging.info("Extraindo dados dos repositórios da Spotify...")
    spotify_rep = DadosRepositorios('spotify')
    ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()
    logging.info("Dados da Spotify extraídos com sucesso: %s linhas.", len(ling_mais_usadas_spotify))

except Exception as e:
    logging.error("Erro durante o processo de extração: %s", e)

logging.info("Processo de ETL concluído.")

# Salvando os dados
try:
    ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv', index=False) # type: ignore
    ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv', index=False) # type: ignore
    ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv', index=False) # type: ignore
    logging.info("Arquivos CSV salvos com sucesso na pasta 'dados/'.")
except Exception as e:
    logging.error("Erro ao salvar os arquivos CSV: %s", e)

#Desafio final: faltou extrairmos dados referentes à empresa Apple, que também era uma de nossas demandas. Sendo assim, utilizando as classes criadas até aqui, realize o processo de ETL para extrair os dados das linguagens de programação utilizadas nos repositórios da Apple.
try:
    apple_rep = DadosRepositorios('apple')
    ling_mais_usadas_apple = apple_rep.cria_df_linguagens()
    ling_mais_usadas_apple.to_csv('dados/linguagens_apple.csv', index=False)
    logging.info("Dados da Apple extraídos e salvos com sucesso: %s linhas.", len(ling_mais_usadas_apple))
except Exception as e:
    logging.error("Erro ao processar os dados da Apple: %s", e)
