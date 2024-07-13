import requests

url = "http://www.baidu.com"
resp = requests.get(url)

print(resp.status_code)
print(resp.text)

