def mergeSort(array):
    # Write your code here.
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    array = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))
    array = array + left + right
    return array


print(mergeSort([8, 5, 2, 9, 5, 6, 3]))
