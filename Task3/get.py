import requests

url = "https://httpbin.org/get"
payload = {"key1": "value1", "key2": "value2"}
r = requests.get(url, params=payload)
print(r.url)
print(r.status_code)
print(r.content)
print(r.text)
print(r.headers)
