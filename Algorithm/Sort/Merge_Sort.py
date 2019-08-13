#Python program for implementation of Merge Sort
#Idea:
# 1. Divide the original list of n/2 into two list of n/2 elements(Chia day gom n phan tu thanh 2 day, moi day n/2 phan tu)
# 2. Recursively merge sort these two lists (De quy merge sort cho moi list)
# 3. Merge the two sorted lists (Tron hai day con da duoc sap xep gom tat ca cac phan tu cua hai day con)

def merge(arr, l, m, r):
    n1 = m - l + 1 #So luong phan tu day con 1
    n2 = r - m  #So luong phan tu day con 2

    #create temp arrays
    L = [0] * n1
    R = [0] * n2

    #Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    #Merge the temp arrays back into arr[l...r]
    i = 0  #Initial index of first subarray
    j = 0  #Initial index of second subarray
    k = l  #Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    #Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    #Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        #devide into two list
        m = (l + r - 1) / 2

        #sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        #merge two list
        merge(arr, l, m, r)


#main program
import timeit

arr = [1, 9, 10, 23, 3, 45, 6, 7, 13, 60, 8]
n = len(arr)
print('Original array is: ')
print(arr)

start = timeit.default_timer()
mergeSort(arr, 0, n - 1)
stop = timeit.default_timer()
print('\nSorted array is: ')
print(arr)
print('Time to process is: ', stop-start)
