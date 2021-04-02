import requests


def client():

    # data = {'username': 'teste',
    #         'email': 'testeTeste@rest.com',
    #         'password1': 'TesteTeste123',
    #         'password2': 'TesteTeste123'}

    # response = requests.post(
    #     'http://127.0.0.1:8000/api/rest-auth/registration/', data=data)

    token_h = 'Token 186f91a3e73f35f7848df2f9b26d0206e926c853'
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
