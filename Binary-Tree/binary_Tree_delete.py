from __future__ import print_function

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

#inOrder traversal of binary tree
def inOrder(temp):
    if (not temp):
        return
    inOrder(temp.left)
    print(temp.data, end=' ')
    inOrder(temp.right)

#function to delete th given deepest node(d_node) in BT (Xoa nut sau nhat trong BT)
def delete_Deepest(root, d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

#function to delete element in BT
def deletion(root, key):
    if root == None:
        return None
    #if root is leaf
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root

    key_node = None
    q = []
    q.append(root)
    #Tim node co chua dat == key
    while (len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if key_node:
        x = temp.data
        delete_Deepest(root, temp)
        key_node.data = x
    return root


if __name__ == '__main__':
    root = Node(10)
    root.insert(11)
    root.insert(7)
    root.insert(12)
    root.insert(9)
    root.insert(15)
    root.insert(8)
    print("InOrder traverse before deletion: ")
    inOrder(root)
    key = 11
    root = deletion(root, key)
    print()
    print("InOrder traverse after deletion: ")
    inOrder(root)
