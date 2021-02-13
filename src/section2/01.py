import requests as req

def main():
    response = req.get("https://api.exchangeratesapi.io/latest")
    print(f'Status Code: {response.status_code}')
    print(f'Status Code: {response.headers["Content-Type"]}')

    if response.status_code != 200:
        print(f'Status Code: {response.status_code} \n')
        print(f'There was an error!')

    data = response.json()
    print(f'Json Data: {data}')

if __name__ == "__main__":
    main()