def min_list(L):
    if len(L) == 1:
        return L[0]
    result=L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
    return result

print(min_list([5,3,5,6,1]))
