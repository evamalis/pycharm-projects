import requests
import json

r = requests.get('https://api.github.com')

d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

print(type(d))
print(d['following_url'])
# обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

r = requests.post('https://httpbin.org/post', data = {'key':'value'}) # отправляем пост запрос
print(r.content)

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(
    data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)