import redis

red = redis.Redis(
    host='redis-17269.c1.us-central1-2.gce.cloud.redislabs.com',
    port=17269,
    password='15R2uqRgfl8BkBALPJama7Vhw27owewl'
)

import json

cont = True

while cont:
    action = input('action:')
    if action == 'write':
        name = input('name:')
        phone = input('phone:')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:')
        phone = red.delete(name)
        if phone:
            print(f"{name}\'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break