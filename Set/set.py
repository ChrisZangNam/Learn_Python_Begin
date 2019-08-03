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
