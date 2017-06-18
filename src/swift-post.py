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
                        "id": "b3c26c9b0a3f47a584211908c643812a",
                        "password": "L2yLC~BZ[H/Mzd~1"
                    }
                }
            },
            "scope": {
                "project": {
                    "id": "c281af0f80fc4410a02dfe9167a3f284"
                }
            }
        }
    }'''

    response = requests.post(url, data=data, headers=headers)
    #print (response.json())
    #print (response.headers)
    #print (response.headers['X-Subject-Token'])
    #print (response.json()['token']['catalog'][0]['endpoints'][0]['url'])

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
    headers = {'X-Auth-Token': token, 'Content-Type': 'text/plain'}
    params = {'file': 'python-test.txt'}

    with open('./python-test.txt') as textFile:
        mydata = textFile.read()
        files = {'python-test.txt': mydata}
        response = requests.put(endpoint, headers=headers, files=files)
        print (response.status_code)
        print (response.headers)
        print (response.text)

if __name__ == "__main__":
    auth_resp = swift_auth()
    swift_get(auth_resp)
    swift_put(auth_resp)
