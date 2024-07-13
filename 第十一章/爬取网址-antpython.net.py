import requests

url = "http://antpython.net"
r = requests.get(url)
print(r.status_code)

with open("antpython.html", "w", encoding='utf8') as f:
    f.write(r.text)

