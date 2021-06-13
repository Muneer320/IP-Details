from urllib.request import urlopen
import json
import time

ip = '123.136.206.4'
api_key = 'at_Mso1iu0ftEbT8FtKJgt8HER8HRdfa'

url = f'https://geo.ipify.org/api/v1?apiKey={api_key}&ipAddress={ip}'
response = urlopen(url)
data_json = json.loads(response.read())

# print(data_json)

for x in data_json:
    print(x, " : ", data_json[x])

time.sleep(5)