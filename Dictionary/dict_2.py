#Cac phuong thuc vw Dictionary

#1. keys() : Tra ve mot list cac key cua Dict

ellen = {"name": "Ellen DeGeneres", "age": "60", "title": ["comedian", "actress"]}
list_key = ellen.keys()
print(list_key)

#2. values(): tra ve mot list cac value cua dict

list_val = ellen.values()
print(list_val)

#3. items(): Tra ve mot list cac tuple, moi tuple chua mot cap key-value
list_item = ellen.items()
print(list_item)

#4. get(key):
#           - Tra ve value cua key
#           - Tra ve None neu key ko ton tai

print(ellen["age"])
# print(ellen["wife"])
print(ellen.get("age"))
print(ellen.get("wife"))

#5. copy():
#         - Tra ve mot ban copy nong (shallow)- copy 1 tang
#         - dict moi duoc luu tru tren mot o nho moi

tomcuirse = {"name": "Tom Cuirse", "from": "America", "height": "1.7m"}
spoof_tomcuirse = tomcuirse.copy()
print(spoof_tomcuirse)
print(tomcuirse is spoof_tomcuirse)  #Giong nhua nhung luu o 2 o nho khac nhau

#   a. copy nong (shallow)

sontungMTP = {
              "name": "Son Tung MTP",
              "age": 25,
              "genre":{
                    "name": "MTP Entertaiment",
                    "song": ["Hay trao cho anh",
                      "Chay Ngay Di",
                      "Lac Troi",
                      "Noi nay co anh"]
                    }
             }

sontungMTP_copy = sontungMTP.copy()
print(sontungMTP_copy)
print(sontungMTP_copy is sontungMTP)
print(sontungMTP_copy["genre"] is sontungMTP["genre"])  #"genre" van chua duoc copy sang mot dict moi ma van tro ve o nho ban dau
#he qua:
sontungMTP_copy["genre"]["from"] = "mid-1950s"
print(sontungMTP)  #--> gia tri cua genre trong bien ban dau cung bi thay doi khi thay doi trong ban copy

#Giai phap: sd copy sau

#    b. copy sau(deep)
import copy
sontungMTP_copy_deep = copy.deepcopy(sontungMTP)
sontungMTP_copy_deep["genre"]["year"] = 2012
print(sontungMTP)
print(sontungMTP_copy_deep)


### Cac ham trong Diction

#1. len() : Tra ve so luong phan tu trong dict(so cap key-value)
print(len(sontungMTP))

#2. for in

for key in sontungMTP:
    print("%s - %s" % (key, sontungMTP[key]))
