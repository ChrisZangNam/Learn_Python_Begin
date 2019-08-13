'''
1. Pick an element, called a pivot, from the original list

2.  Rearrange the list so that:
    - All elements less than pivot come before the pivot
    - All elements greater or equal to pivot com after pivot

3. Here, pivot is in the right position in the final sorted list(it is fixed)

4. Recursively sort the sub-list before pivot and thee sub-list after pivot
'''

import timeit

def partition(arr, l, r, indexPivot):
    pivot = arr[indexPivot]
    arr[indexPivot], arr[r] = arr[r], arr[indexPivot]

    storeIndex = l

    i = l
    while i <= r - 1:
        if arr[i] < pivot:
            arr[storeIndex], arr[i] = arr[i], arr[storeIndex]
            storeIndex += 1
        i += 1

    arr[storeIndex], arr[r] = arr[r], arr[storeIndex]

    return storeIndex

def quickSort(arr, l, r):
    if l < r:
        index = (l + r) / 2
        index = partition(arr, l, r, index)
        if l < index:
            quickSort(arr, l, index - 1)
        if index < r:
            quickSort(arr, index + 1, r)


arr = [1, 9, 10, 23, 3, 45, 6, 7, 13, 60, 8]
n = len(arr)
print('Original array is: ')
print(arr)

start = timeit.default_timer()
quickSort(arr, 0, n - 1)
stop = timeit.default_timer()
print('\nSorted array is: ')
print(arr)
print('Time to process is: ', stop-start)
