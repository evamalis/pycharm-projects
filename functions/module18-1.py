import requests
import json

r = requests.get('https://baconipsum.com/api/?callback=?')

data = {'type': 'all-meat', 'paras' : '2', 'format':'json'}

requests.post('https://baconipsum.com/api/?callback=?', data)
d = json.loads(r.content)
print(type(d))
print(r.content)

