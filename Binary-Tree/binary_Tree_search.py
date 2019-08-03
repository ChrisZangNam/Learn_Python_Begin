class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #Insert
    def insert(self, data):
        #Compare the new value with the parent node
        if self.data:
            if data < self.data:
              if self.left is None:
                  self.left = Node(data)
              else:
                  self.left.insert(data)
            elif data > self.data:
              if self.right is None:
                  self.right = Node(data)
              else:
                  self.right.insert(data)
        else:
            self.data = data

    #find method to compare the value with node
    def findVal(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findVal(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findVal(lkpval)
        else:
            print(str(self.data) + " is found")

    #Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root = Node(16)
root.insert(10)
root.insert(20)
root.insert(5)
root.insert(15)
root.insert(22)
root.insert(8)

print(root.findVal(30))
print(root.findVal(10))
