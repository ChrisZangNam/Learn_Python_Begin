def Bubble_Sort(list, n):
    i = 0
    while(i < n - 1):
        j = n - 1
        while(j > i):
            if(list[j] < list[j - 1]):
                list[j - 1], list[j] = list[j], list[j - 1]
                j -= 1
            i += 1

l = [1,4,6,2,8,9,3,5,10]
