#Data Hiding
# In Python, we use double underscore (Or __) before the attributes name
# and those attributes will not be directly visible outside


class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 10

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)

    # Driver code


myObject = MyClass()
# myObject.add(2)
# myObject.add(5)

# This line causes error
# print(myObject.__hiddenVariable)
print(myObject._MyClass__hiddenVariable)

#Printing Objects
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a: %s b: %s" %(self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s, " \
                "b is %s" %(self.a, self.b)

#Driver code
t = Test(1234, 5678)
print(t) #call __str__()
print([t]) #call __repr__()


# Important Points about Printing

#If no __str__ method is defined, print t(or print str(t)) uses __repr__
class Test_1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a: %s, b: %s" %(self.a, self.b)

t = Test_1(12,34)
print(t)

# If no __repr__ method is defined then the default is used.
class Test_2:
    def __init__(self, a,b):
        self.a = a
        self.b=b

t = Test_2(12,34)
print(t)




