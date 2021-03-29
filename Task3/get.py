import requests

url = "https://httpbin.org/get"
payload = {"key1": "value1", "key2": "value2"}
r = requests.get(url, params=payload)
print(r.url)
print(r.status_code)
# prints the content in bytes
print(r.content)
# prints the content in string
print(r.text)
# prints the headers from which we can see the content type and other information
print(r.headers)


if r.status_code == 200:
    print("Success!")
else:
    print("No connection.")

# Convert to a dictionary
print(r.json())
