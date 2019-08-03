#####Set : Tap hop
# Tinh chat:
#     - Tap hop cac phan tu sap xep ko co thu tu, cac gia tri ko lap lai
#     - Moi phan tu la doc nhat(unique) va phai la bat bien(immutable)
#     - Ban than Set lai kha bien(muntable)-co them, xoa phan tu cua set

#1. Init Set

#   Method 1:

number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
mix_set = {'Nam', 7, 3, 1999, (5, 7, 8)}
print(number_set)
print(mix_set)
#Cac kieu du lieu trong set phai bat bien: Int, float, boolean, tuple, string
#python bao loi neu dat mot bien kha biet trong set(ex: List,...)

#   Method 2:

foods = set()
foods.add("Toast")
print(foods)
apple = set("apple")
print(apple)

Days = set(["mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
print(Days)

#2. Asscessing Values in a Set

for d in Days:
    print(d)

#3. Cac phuong thuc trong set

#3.1 add(): Them mot phan tu vao set
breakfast = {"eggs", "bacon", "sausage", "toast", "cereal", "milk", "muffin"}
breakfast.add("coffee")

print(breakfast)

#3.2 remove() : Xoa 1 phan tu khoi Set, throw error neu phan tu ko ton tai trong Set
breakfast.remove("sausage")
print(breakfast)
# breakfast.remove("pho")

#3.3 discard() : xoa 1 phan tu khoi Set, neu ko ton tai phan tu trong Set thi ko throw error
breakfast.remove("bacon")
breakfast.discard("pho")
print(breakfast)

#3.4 union() : Tra ve hop cua hai tap hop
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 7, 8, 9}
C = A.union(B)
C = B.union(A)
C = A | B
print(C)

#3.5 intersection() : Tra ve giao 2 tap hop
C = A.intersection(B)
print(C)
C = B.intersection(A)
print(C)
C = A & B
print(C)

#3.6 difference() : Tra ve hieu hai tap hop
A = {"Ha Anh Tuan", "My Tam", "Erik", "Duc Phuc"}
B = {"Thanh Ha", "Ha Anh Tuan", "Issac"}
C = A.difference(B)
print(C)
C = A - B
print(C)

#4. Frozenset
#   Neu tuple la mot immutable thi fronzenset la mot #immutable set. Ta ko the xoa, them phan tu trong Set
A = frozenset([1, 2, 3, 4])
A.add("10")
