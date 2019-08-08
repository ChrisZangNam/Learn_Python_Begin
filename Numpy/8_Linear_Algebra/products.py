#Nhan ma tran va vector

import numpy as np

#1.inner():Tich vo huong cua 2 vector
#   Dieu kien: 2 vector phai cung chieu voi nhau

#Cong thuc:  x[] * y[] = xT*y = x1y1 + x2y2 + .... xn * yn
print('Nhan 2 vector')
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print 'A = ', A, ', B = ', B
print'A * B = ', np.inner(A, B)

#2. dot() : Tich vo huong 2 ma tran
#   Dieu kien: A: R(mxn), B: R(nxp)
#   Ket qua C = A*B = R(mxp)
print('\nNhan 2 ma tran')
A = np.array([
    [1, 2],
    [3,4]
])
B = np.array([
    [5, 6],
    [7,8]
])
C = A.dot(B)
print'A = '
print A
print'B = '
print B
print'dot(A,B) = '
print C
C = np.dot(A, B)
print(C)

print'dot(B,A) = '
C = B.dot(A)
print(C)
C = np.dot(B, A)
print(C)

#vdot() : Nhan tung phan tu tuong ung roi tong lai.
#   Dieu kien: A, B cung kich thuoc
print'A = '
print A
print'B = '
print B
print('vdot(A,B) = ')
print(np.vdot(A,B))

#tensordot(): tuong tu vdot()
print'A = '
print A
print'B = '
print B
print('tensordot(A,B) = ')
print (np.tensordot(A,B))
