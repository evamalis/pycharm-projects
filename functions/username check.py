yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper


USERS = ['admin', 'guest', 'director', 'root', 'superstar']

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")


def has_access(func):
    def wrapper():
        if username in USERS:
            print("Username is correct")
            func()
        else:
            print("User not found")
    return wrapper



@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()