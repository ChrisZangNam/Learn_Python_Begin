#A simple example class
class Test:

    # A sample method
    def fun(self):
        print("Hello")

#Driver code
obj = Test()
obj.fun()

#The _init_method
#The _init_method is run as soon as an object of a class instantiated.
#The method is useful to do any initialization you want to do with your object

class Person:

    #init method or constructor
    def __init__(self, name):
        self.name = name

    #sample mathod
    def say_hi(self):
        print("Hello, my name is ", self.name)

p = Person("Andrew")
p.say_hi()

#Class and Instance Variables (Or attributes)-Lop va Bien (hoac cac thuoc tinh)

class CSStudent:

    #Class Variable
    stream = 'cse'

    #the init method or constructor
    def __init__(self, roll):

        #Instance Variable
        self.roll = roll

    #Adds an instance variable
    def setAddress(self, address):
        self.addess = address

    #Retrieves instance variable
    def getAddress(self):
        return self.addess



a = CSStudent(101)
b = CSStudent(102)

a.setAddress("Noida, UP")

print(a.stream)
print(b.stream)
print(a.roll)

print(CSStudent.stream)
print(a.getAddress())

#Create an empty class
class Test:
    pass










