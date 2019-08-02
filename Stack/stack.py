#Khoi tao mot Stack voi mot bien thuc the la mot list rong
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, dataVal):
        #Use list append method to push element
        if dataVal not in self.stack:
            self.stack.append(dataVal)
        else:
          return False

    def pop(self):
        #use list pop method to remove element
        if len(self.stack) <= 0:
            return ('No element in the Stack')
        else:
            return self.stack.pop()

    #Look at the top of the Stack
    def peek(self):
        return self.stack[-1]

    #print all elements
    def stackprint(self):
        if len(self.stack) <= 0:
            print("Stack is empty")
        else:
            for elem in self.stack:
                print(elem)


stack = Stack()
stack.push('Mon')
stack.push('Tue')
stack.push('Wed')
stack.push('Thu')
stack.push('Fri')
stack.push('Sat')
stack.push('Sun')

stack.stackprint()
print('------------')
print(stack.peek())
print('------------')
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())
print('----------')
stack.stackprint()
