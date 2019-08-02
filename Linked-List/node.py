#1. Create a node
class Number:
    def __init__(self, val):
        self.val = val
        self.nextVal = None

number1 = Number(1) #value = 1
number2 = Number(2) #value = 2
number3 = Number(3) #value = 3

number1.nextVal = number2
number2.nextVal = number3

#2. Access to node of element
print(number1.nextVal.val)  #number2
print(number2.nextVal.val)  #number3

#3. Read all node
current_Node = number1
while current_Node:
    print(current_Node.val)
    current_Node = current_Node.nextVal
