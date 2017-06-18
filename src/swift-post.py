# coding: utf-8
import requests

def swift_auth():
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
    return response

def swift_get(response):
    token = response.headers['X-Subject-Token']
    endpoint = response.json()['token']['catalog'][7]['endpoints'][3]['url']
    endpoint = endpoint + '/test'
    headers = {'X-Auth-Token': token}

    response = requests.get(endpoint, headers=headers)
    print (response.status_code)
    print (response.headers)
    print (response.text)

def swift_put(response):
    token = response.headers['X-Subject-Token']
    endpoint = response.json()['token']['catalog'][7]['endpoints'][3]['url']
    endpoint = endpoint + '/test/python-test.txt'
    headers = {'X-Auth-Token': token, 'Content-Type': 'text/html; charset=UTF-8'}

    with open('./python-test.txt') as myfile:
        mydata = myfile.read()
        response = requests.put(endpoint, headers=headers, data=mydata)
        print (response.status_code)
        print (response.headers)
        print (response.text)

if __name__ == "__main__":
    auth_resp = swift_auth()
    swift_get(auth_resp)
    swift_put(auth_resp)
