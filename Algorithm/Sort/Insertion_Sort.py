def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        #Move elements of arr[0...i-1] that are
        #greater than key, to one position ahead
        #of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [1,4,6,2,8,9,3,5,10,7]
print(arr)
insertionSort(arr)
print(arr)
