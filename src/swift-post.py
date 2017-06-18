# coding: utf-8
import requests

url = 'https://lon-identity.open.softlayer.com/v3/auth/tokens'
headers={'Content-Type': 'application/json'}
data = '''{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "id": "",
                    "password": ""
                }
            }
        },
        "scope": {
            "project": {
                "id": ""
            }
        }
    }
}'''

response = requests.post(url, data=data, headers=headers)
#print (response.json())
#print (response.headers)
#print (response.headers['X-Subject-Token'])
#print (response.json()['token']['catalog'][0]['endpoints'][0]['url'])

token = response.headers['X-Subject-Token']
endpoint = response.json()['token']['catalog'][7]['endpoints'][3]['url']
headers = {'X-Auth-Token': token}

response = requests.get(endpoint, headers=headers)
print (response.status_code)
print (response.headers)
print (response.text)
