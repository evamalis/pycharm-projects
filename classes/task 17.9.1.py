numbers = input('input numbers:').replace(" ", "")
rndom_num = input('input random number:')

numbers = list(numbers)

def sort(self):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


sort(numbers)
print('Sorted numbers:', numbers)


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


result = binary_search(numbers, rndom_num, 0, len(numbers) - 1)
x = result - 1
y = result or result + 1
if not result:
    print("No element")
else:
    print(x, y)
