
#Create Node
class Node:
    def __init__(self, dataVal=None):
      self.dataVal = dataVal
      self.nextVal = None

#Create Linked List
class LinkedList:
    #create list
    def __init__(self):
        self.headVal = None

    #traverse list
    def listprint(self):
        current_Node = self.headVal
        while current_Node:
            print(current_Node.dataVal)
            current_Node = current_Node.nextVal

    #insert at the Beginning of the List
    def Insert_First(self, newData):
        new_Node = Node(newData)
        new_Node.nextVal = self.headVal
        self.headVal = new_Node

    #insert at the end of the List
    def Insert_Last(self, newData):
        new_Node = Node(newData)

        if self.headVal is None:
            self.headVal = new_Node
            return

        laste = self.headVal
        while laste.nextVal:
            laste = laste.nextVal

        laste.nextVal = new_Node

    #insert in between two Data Nodes
    def Insert_Between(self, mid_Node, newData):
        if mid_Node is None:
            print('The mentioned node is absent')
            return

        new_Node = Node(newData)
        new_Node.nextVal = mid_Node.nextVal
        mid_Node.nextVal = new_Node

    #Remove an item  form a Linked List
    def Remove_Node(self, removeKey):
        HeadVal = self.headVal

        if (HeadVal is not None):
            if (HeadVal.dataVal == removeKey):
                self.headVal = HeadVal.nextVal
                HeadVal = None
                return

        while (HeadVal is not None):
            if (HeadVal.dataVal == removeKey):
                break
            prev = HeadVal
            HeadVal = HeadVal.nextVal

        if (HeadVal == None):
            return

        prev.nextVal = HeadVal.nextVal
        HeadVal = None



list = LinkedList()
list.headVal = Node('Tue')
e3 = Node('Wed')
e4 = Node('Thus')

list.headVal.nextVal = e3
e3.nextVal = e4
list.listprint()
print('----------')

list.Insert_First('Mon')
list.listprint()
print('----------')
list.Insert_Last('Fri')
list.listprint()
print('----------')
list.Insert_Between(list.headVal.nextVal, 'Sat')
list.listprint()
print('----------')

list.Remove_Node('Sat')
list.listprint()
