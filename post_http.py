import requests
from requests.exceptions import HTTPError
import json
url = 'https://httpbin.org/post'
try:
    data = {'key1':'value1'}
    #response = requests.post(url, data=data)
    response = requests.post(url, json=json.dumps(data))
    #print(response.status_code)
    print(response.text)
except HTTPError as e:
    print(f'erro: {e}')
