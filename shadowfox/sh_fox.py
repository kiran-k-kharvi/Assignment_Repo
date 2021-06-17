import requests

def my():
    payload = {"test": "true"}
    Headers = {"Authorization": "test-tokens"}
    x = requests.post(url="https://google.com",headers=Headers,data=payload)
    print(x.status_code)
    print(x.reason)

my()