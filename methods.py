import requests
from requests.exceptions import HTTPError

url = 'https://httpbin.org/get'
url_del = 'https://httpbin.org/delete'
url_post = 'https://httpbin.org/post'
url_put = 'https://httpbin.org/put'

try:
    #requeste get
    response = requests.get(url)
    #
    #mostra as opções disponiveis na url
    response_op = requests.options(url)
    print(response_op.status_code)

    #deltando data
    print(requests.delete(url_del).status_code)

    #enviando dados para o server
    print(requests.post(url_post, data={'key1':'value1', 'key2':'value2'}).status_code)

    #editando datos
    print(requests.put(url_put, data={'key1':'value101'}).status_code)

    #obtendo o header da url
    print(requests.head(url))

except HTTPError as e:
    print(f'erros {e}')
except Exception as e:
    print(f'error: {e}')
