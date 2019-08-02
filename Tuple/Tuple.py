#Mo dau ve Tuple

#duoc gioi han boi cap ngoac ()
#cac phan tu cua tuple duoc ngan cach boi dau ,
#tuple co kha nang chu moi gia tri
#toc do truy xuat cua tuple nhanh hon list
#dung luong chiem trong bo nho nho hon list
#bao ve du lieu cua ban se khong thay doi
#co the dung lam key cua dictionary


tup = (1,1,2,5,6,'Kteam', 7,7, (2,5,6))
tup1 = (1) #Khong duoc tinh la mot tuple, la mot int
tup2 = (1,)
print(tup1, tup2)
print('------------------------------')
tup = (i for i in range(10)) #generator object from 0 ->9
a = tuple(tup)
print(tup)
print(a)

#=============================================
#Cac toan tu cua tuple giong voi chuoi

tup1 = (1,2,3)
a = tup1 + (2,4,6)
print(a)
#nhan tuple voi mot so
a = tup1*3
print(a)
# in : kiem tra mot phan tu co trong tuple hay ko
a = 3 in tup1
print(a)

#truy xuat toi mot phan tu
a = tup1[0]
b = tup1[2]
c = tup1[-1]
print(a, b, c)
#do dai tuple
a = len(tup1)
print(a)
a = tup1[:-1]
print(a)

tup = [1,5,9,4]
tup[0] = 'Kteam'
tup = (1,5,9,4)

#ma tran
tup = ((1,2,3,4), (4,5,6,7),(7,8,9,10))

#Hash object : kieu du lieu ko the thay doi du lieu ben trong
#Tuple ko cho phep ban sua chua noi dung ben trong nos, khac voi list

#=============================================
#Cac phuong thuc cua Tuple

# count : Tim so lan suat hien cua 1 phan tu trong tuple
tup = (1,2,3,4,4,5,6,4,7)
a = tup.count(4)
print(a)
# index : tra ve vi tri xuat hien dau tien cua phan tu
a = tup.index(6)
print(a)
print('------------------------------')

#=============================================
#Cac ham lien quan den Tuple

# map(): Tra ve mot list dua tren mot dieu kien cho truoc
tuple = (1, 2, 3, 4, 5)
def square(x):
    return x ** 2

result = map(square, tuple)
print(result)

# filter(): Tra ve mot List duoc loc theo mot dieu kien cho truoc

tuple = ('Anh', 'Thu', 'Son', 'Dung', 'An', 'Quynh', '1', '2', '8')

#tao ham loc chuoi la cac chu cai
def filter_Alphabet(elem):
    return elem.isalpha()

#tao ham loc chuoi la cac chu so
def filter_Digit(elem):
    return elem.isdigit()

res1 = filter(filter_Digit, tuple)
res2 = filter(filter_Alphabet, tuple)

print(res1)
print(res2)
print(type(res1))

# enumerate() : Tra ve mot enumerate Object
#(la mot lis chua cac phan tu tuple moi,
# tuple moi bao gom gia tri cua phan tu
# tuple ban dau va gia tri chi muc cua no)
#Thuong sd khi muon sd ca gia tri va chi muc trong tuple

shoes = ('Addidas', 'Nike', 'Puma', 'Lining')
print(list(enumerate(shoes)))

# reversed(): Tra ve mot reverse Object trong do cac phan tu da duoc dao nguoc vi tri
fishes = ('Tuna', 'LargeMouth', 'Carp', 'RedFish')
print(type(fishes))
res = list(reversed(fishes)) #co the thay list = tuple
print(res)

# zip(): Nhom cac phan tu trong cac tuple o vi tri co chi muc tuong ung,
#moi nhom tro thanh mot tuple dong thoi la mot phan tu tuong ung cua mot list moi

equiqments = ('computer', 'video display', 'typerwritter')
rooms = ('living room', 'kitchen', 'guest room', 'bath room')
result = zip(equiqments, rooms)
print(result)

# sorted(): Tra ve mot list ma trong do cac phan tu duoc sap sep theo ky tu dau tien
actions = ('pack', 'stand', 'throw', 'tie', 'run', 'jump', 'hug', 'shave', 'eat', 'drink')
print(sorted(actions))

#  sum():
#Tra ve tong cac phan tu co trong tuple
#Throw error neu mot phan tu trong tuple khong phai dang so
tup1 = (1, 2, 3, 5, 10)
tup2 = (1,2,3, 'a', 'chris')
print(sum(tup1))
print(sum(tup2))
