import requests


def client():
    token_h = 'Token 8f83bc361106ddbda1274e1b9a18bc05e8a320c2'
    # credentials = {'username': 'admin', 'password': 'admin'}

    # response = requests.post(
    #     'http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)

    headers = {'Authorization': token_h}

    response = requests.get(
        'http://127.0.0.1:8000/api/profiles/', headers=headers)

    print('Status code:', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
