import requests
from requests.exceptions import HTTPError
url = 'https://httpbin.org/get'
try:
    response = requests.get(url)
    #retorna url informada
    print(response.url)
    #codificação do requisição
    print(response.encoding)
    #header da requisição
    print(response.headers)
    #acessando os atributos do header, retorna a dat
    print(response.headers['Date'])
    #outra forma de acesso
    print(response.headers.get('Date'))
    #
except HTTPError as e:
    print(f'error {e}')
