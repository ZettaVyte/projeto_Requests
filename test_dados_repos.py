from dados_repos import DadosRepositorios

def test_inicializacao_da_classe():
    # 1. Preparação (Arrange)
    empresa_teste = "netflix"

    #2. Ação (Act) - Rodamos o código real
    objeto = DadosRepositorios(empresa_teste)

    #3. Verificação (Assert) - Validamos o resultado

    #Quero garantir que o o atributo owner é igual a 'netflix'
    assert objeto.owner == empresa_teste

    #Garantir que a URL base da API do GitHub está correta
    assert objeto.api_base_url == 'https://api.github.com'


def test_headers_tem_token():
    # Testamos se o header de autenticação foi criado
    objeto = DadosRepositorios("amzn")

    # Verificamos se existe a chave 'Authorization' no dicionário headers
    assert 'Authorization' in objeto.headers

    #Verificamos se começa com 'token'
    assert objeto.headers['Authorization'].startswith('token')
