import requests

url = "https://httpbin.org/patch"
payload = {"FirstName": "John", "LastName": "Smith"}
r = requests.patch(url, data=payload)
print(r.status_code)
print(r.text)
