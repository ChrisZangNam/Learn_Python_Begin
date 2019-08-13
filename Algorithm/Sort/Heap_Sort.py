#Heap Sort

import timeit

def Heapify(a, i, n):
    #array to be heapified is a[i....n]
    L = 2 * i #Left child
    R = 2 * i + 1  #Right child
    max = i

    if L < n and a[L] > a[i]:
        max = L
    if R < n and a[R] > a[max]:
        max = R
    if max != i:
        a[i], a[max] = a[max], a[i]
        Heapify(a, max, n)

def heapSort(a, n):
    n = len(a)

    #Build a maxheap:
    for i in range(n, -1, -1):
        Heapify(a, i, n)

    #One by one axtract elements
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        Heapify(a, 0, i)


arr = [1, 9, 10, 23, 3, 45, 6, 7, 13, 60, 8]
n = len(arr)
print('Original array is: ')
print(arr)

start = timeit.default_timer()
heapSort(arr, n)
stop = timeit.default_timer()
print('\nSorted array is: ')
print(arr)
print('Time to process is: ', stop-start)
