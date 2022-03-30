def even(x):
    return x%2==0

result = filter(even, [1,2,3,4,5,6])

print(list(result))

