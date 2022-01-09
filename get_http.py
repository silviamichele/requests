import requests
from requests.exceptions import HTTPError
#import json
url = 'https://httpbin.org/get'
try:
    response = requests.get(url)
    #retorna o status da requisição
    print(response.status_code)
    #conteudo da página contida na url
    #outras opções response.content e response.json()
    print(response.text)
except HTTPError as e:
    print(e)
