#Dictionary la dkieu du lieu dang tu dien
#Bao gom nhieu cap key-value
#Trong do key: tu, val: y nghia
#key - val duoc phan cach nhau boi dau :, cac cap key-val duoc phan cach boi dau ,
#Dictionary la kieu du lieu kha bien(mutable)

#1. Create a Dictionary
  #Method 1

soobin = {"age": 27, "song": ["Neu Ngay Ay"]}
sontungMTP = {
              "name": "Son Tung MTP",
              "birth year": 1994,
              "song": ["Hay trao cho anh",
                        "Chay Ngay Di",
                        "Lac Troi",
                        "Noi nay co anh"],
              "mother": {
                  "name": "Pham Thi Thanh Binh"
              }
            }
addresses = {1: "Thanh Nhan", 2: "Hai Ba Trung", 3: "Ha Noi"}
rooms = {("pillows", "carpet", "computer"): "bedroom"}

  #Method 2:

dict([("name", "Vu Cat Tuong"), ("year", 1992), ("albums", ["Dong", "Vet mua", "Yeu xa", "If"])])

  #Method 3:
  #(Trong truong hop cac key deu la chuoi)

dict(type="zoo", activities=["skipping rope", "playting see-saw", "swinging", "flying kite", "blowing bubbies", "sliding"])

  #Method 4:
{x: x + " dep trai" for x in ["Duong", "Kiem", "Nam"]}

#2. Kieu du lieu cua Key va Value
#   Key: la kieu du lieu bat bien(immutable): chuoi(string), number, tuple
#        tuple la key trong trh chua cac gia tri bat bien(chuoi, so, tuple,...)
#   Value: da dang, co the la bat cu kieu du lieu nao


#3. Acessing Value in dictionary

print "Age of Soobin is: ", soobin["age"]
print "Song of SonTung is: ", sontungMTP["song"]
print "Name of Sontung's Mother is: ", sontungMTP["mother"]["name"]

#trong trh 2 ley giong nhau thi truy cap den phan thu cuoi
Nam = {"name": "Kieu Dang Nam", "name": "Chris Zang Nam"}
print(Nam["name"])

print(list(sontungMTP))  #lieu ke cac key trong dict

#4. Updating Dictionary

ironman = {"name": "Tony Stark", "seasons": 3, "publisher": "unknow"}
ironman["publisher"] = "Marvel Comics"
print(ironman)

#5. Delete Dictionary Elements

zara = {"name": "Zara", "founded": 1974, "revenue": "18 billion USD"}
del zara["founded"]
print(zara)

    #Xoa tat ca phan tu
apple = {"name": "Apple", "founded": 1976, "stock price": "$210"}
apple.clear()
print(apple)

    #Xoa hoan toan han dictionary
PMG = {"name": "PMG", "CEO": "Jeanie Hood", "revenue": "110.8 Billion USD"}
del PMG
#print(PMG)
