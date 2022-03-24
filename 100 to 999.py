a=int(input("a:"))
if type(a)==int:
    if 100<a<999:
        if a%2==0:
            if a%3==0:
                print("true")
else:
    print('false')