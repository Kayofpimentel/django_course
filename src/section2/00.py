import requests as req

def main():
    response = req.get("https://www.google.com/ndsanudn")
    print(response.status_code)
    print(response.headers)
    print(response.text)

if __name__ == "__main__":
    main()