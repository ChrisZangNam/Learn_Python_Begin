import numpy as np

number_2D = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(number_2D)

#1. Truy cap hang

print(number_2D[0])  #hang dau tien
print(number_2D[0, ...])
print(number_2D[-1])  #hang cuoi cung
print(number_2D[-1, ...])
#2. Truy cap cot

print(number_2D[:, 0])
print(number_2D[...,0]) #cot dau tien
print(number_2D[:, -1])  #cot cuoi cung
print(number_2D[...,-1])
print(number_2D[:, 2])  #cot o giua
print(number_2D[...,2])
#3. Truy cap mang trong ma tran

awesome = np.array([
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 4, 5, 8, 9, 0],
        [2, 9, 7, 8, 0, 4, 5],
        [9, 6, 4, 9, 3, 7, 2]
    ])

print(awesome.shape)
#Truy cap hang 2 va 3, cot 3 va cot 4
print(awesome[1:3, 2:4])

#4. Truy cap phan tu
print(awesome[0, 1])  #Hang 1, cot 2
print(awesome[0][1])
print(awesome[1, 2])  #Hang 2, cot 3
print(awesome[1][2])

#In cac cot lien tiep, hang lien tiep
print(awesome[..., 2:])
print(awesome[1:, ...])
print('\n')


##Indexing advanced

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]] #chon cac phan tu (0,0), (1,1), (2,0) tu mang x
print(x)
print('\n')
print(y)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('Our array is')
print(x)
print('\n')

rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])

y = x[rows, cols]
print('The corner elements of this array are:')
print(y)

print('\n')
z = x[1:4, 1:3]
print(z)

print('\n')
y = x[1:4, [1, 2]]
print(y)

print('Index Boolean')
y = x[x > 5]
print(y)
