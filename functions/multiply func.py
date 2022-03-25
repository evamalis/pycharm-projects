def mult(*nums):
    p = 1
    for n in nums:
        p=p*n

    return p
print(mult(2,3,4,1,6))