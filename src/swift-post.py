# coding: utf-8
import requests
import credential

def swift_auth():
    cred = credential.credential()
    userId, password, projectId = cred.get()
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
                        "id": "%s",
                        "password": "%s"
                    }
                }
            },
            "scope": {
                "project": {
                    "id": "%s"
                }
            }
        }
    }''' % (userId, password, projectId)

    response = requests.post(url, data=data, headers=headers)
    token = response.headers['X-Subject-Token']
    endpoint = response.json()['token']['catalog'][7]['endpoints'][3]['url']
    return [token, endpoint]

def swift_get(token, endpoint):
    container = endpoint + '/test'
    headers = {'X-Auth-Token': token}

    response = requests.get(container, headers=headers)
    print (response.status_code)
    print (response.headers)
    print (response.text)

def swift_put(token, endpoint):
    put_filepath = endpoint + '/test/python-test.txt'
    headers = {'X-Auth-Token': token, 'Content-Type': 'text/html; charset=UTF-8'}

    with open('./python-test.txt') as myfile:
        mydata = myfile.read()
        response = requests.put(put_filepath, headers=headers, data=mydata)
        print (response.status_code)
        print (response.headers)
        print (response.text)

if __name__ == "__main__":
    token, endpoint = swift_auth()
    swift_get(token, endpoint)
    swift_put(token, endpoint)
