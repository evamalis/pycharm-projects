tickets=int(input('Input the amount of tickets:'))
price=0
for i in range(1,tickets+1):
    age=int(input('Input the age:'))
    if age<18:
        price=price+0
    elif 18<=age<25:
        price=price+990
    else:
        price=price+1390
    print(price)
print("Total amount before discount:", price)
if tickets>=3:
    price=int(price*0.9)
    print("You save 10%")
print("Final amount:", price)


