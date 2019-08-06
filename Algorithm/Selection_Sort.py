'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
'''

import sys

def selectionSort(arr):
    for i in range(len(arr)):

        #find the minimun element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        #Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [1, 4, 6, 2, 8, 9, 3, 5, 10, 7]
print(arr)
selectionSort(arr)
print(arr)
