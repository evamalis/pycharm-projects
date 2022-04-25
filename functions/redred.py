import redis

red = redis.Redis(
    host='redis-17269.c1.us-central1-2.gce.cloud.redislabs.com',
    port=17269,
    password='15R2uqRgfl8BkBALPJama7Vhw27owewl'
)

import json

dict1 = {'key1': 'value1', 'key2': 'value2'} # создаём словарь для записи
red.set('dict1', json.dumps(dict1)) # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1')) # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь

print(type(converted_dict)) # убеждаемся, что получили действительно словарь
print(converted_dict)

red.delete('dict1') # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))