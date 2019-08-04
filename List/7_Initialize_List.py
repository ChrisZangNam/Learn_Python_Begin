#Method 1: Using loop and append()

#for loop
arr = []
for i in range(10):
    arr.append(0)

#while loop
arr = []
i = 0
while (i < 10):
    arr.append(0)
    i = i+1

#Method 2: Using list comprehensions
arr1 = [0 for i in range(10)]

#Method 3: Using * operator
arr2 = [0] * 10

print(arr)
print(arr1)
print(arr2)

###2d Array or matrix
# arr_2d = [[0]*no_of_cols]*no_of_rows
# arr = [[0 for i in range(no_of_cols)] for j in range(no_of rows)]

arr_2d = [[0] * 3] * 2
print(arr_2d)
arr_2d = [[0 for i in range(3)] for j in range(2)]
print(arr_2d)
