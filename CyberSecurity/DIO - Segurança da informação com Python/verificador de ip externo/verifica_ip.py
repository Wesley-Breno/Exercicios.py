import requests
import json

site = requests.get('http://ipinfo.io/json')
json_site = site.json()

with open('ips.json', 'w+') as file:
    file.write(json.dumps(json_site, indent=4))
