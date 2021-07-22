def binary_search(array, item, first, last):
    if first > last:
        return False
    middle = (first + last) // 2
    if array[middle] == item:
        return middle
    elif array[middle] > item:
        last = middle-1
        return binary_search(array, item, first, last)
    else:
        first = middle+1
        return binary_search(array, item, first, last)

array = [33,27,59,67,95,17,48,28,100]
array = sorted(array)
print(binary_search(array, 48, 0, len(array)-1))