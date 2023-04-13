""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 5. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 5 (available in Week 5).

    There will be some ***introductory challenges*** in Week 4, with solutions released in Week 5.
    It is STRONGLY RECOMMENDED you attempt these!

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the Week 5 lab sheet guidance). 
"""

import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def Bin_Tree_find_iterative(self,target):
        cur_node=self.root #will set the current node to the root of the graph
        while cur_node != None: #whilst the current node exists
            if cur_node.data == target: # will check if the current node is equivalent to the target node
                return str(cur_node.data) + " Found data" #will return the current node and a string saying it was found
            elif cur_node.data >target: # will check if the current node is greater than the target
                cur_node=cur_node.left #will move onto the left node if it is greater
            else:
                cur_node=cur_node.right #else will move to the right node if it isn't greater
        return False # will return false if the node doesnt exist

    def Bin_Tree_find_recursive(self,target):
        if self.root: # if the tree exists
            if self._Bin_Tree_find_recursive(target,self.root): # will call the recursive find function
                return True # if it works will return true
            return False # if it doesn't will return false
        else:
             return None # if there is no tree will return false

    def _Bin_Tree_find_recursive(self,target,cur_node):
        if target > cur_node.data and cur_node.right: #will check if the target node is greater than the current node and the node to its right
            return self._Bin_Tree_find_recursive(target, cur_node.right) # if so will return the right node
        elif target < cur_node.data and cur_node.left: #will check if the target is smaller than the current node and left node
            return self._Bin_Tree_find_recursive(target,cur_node.left) # if so will return the left node
        if target == cur_node.data: # checks if the target node is equivalent to the current node
            return True # if it is will return true
   
    def if_left_and_right(self, node):
        delNodeParent= node # will create a parent node varaible which is assinged to what node is
        delNode= node.right # will create a node variable that is assigned to the node on the right
        
        while delNode.left: #whilst the node is the left node will iterate
            delNodeParent = delNode #will make the parent node equivalent to the delNode
            delNode = delNode.left #will make delNode equivalent to the left node

        node.data=delNode.data #will make the main node equivalent to delNode

        if delNode.right: # if delNode is on the right node
            if delNodeParent.data > delNode.data: #will check if the parent node is greater than the current node
                    delNodeParent.left = delNode.right # if so it will make it so the  variable for the node left to the parent is equivalent to the right node
            else:
                delNodeParent.right = delNode.right #else will make the parent node go to the right
        else:
            if delNode.data < delNodeParent.data: #will check if the current node is less than the parent node
                delNodeParent.left = None #if so the left node becomes nothing
            else:
                delNodeParent.right = None #if the current node is greater then the right node becomes nothing

   
    def remove(self,target):

        if self.root is None: #will check is the tree exitsts
            return False #if it doesnt then returns false
        elif self.root.data == target: # will check if the target node is in the tree
            if self.root.left is None and self.root.right is None: # if so will check if there is nothing else on the left and right node
                self.root= None #if there is nothing then the root node becomes nothing
            elif self.root.left and self.root.right is None: #else if the left node has something
                self.root= self.root.left #will make the root become the left
            elif self.root.left is None and self.root.right: #else if the right has something
                self.root=self.root.right #will make the root become the right
            elif self.root.left and self.root.right:#will check if either left or right have something
                self.if_left_and_right(self.root) # will call the if left and right function
        parent = None # will make the parent equivalent to nothing
        node = self.root # will set a node variable that is equivalent to the tree

        while node and node.data != target: #will check that the current node is equivalent to the target and iterate
            parent= node #will make the parent equivalent to the node
            if target < node.data: #checks if the target node is less than the node
                node=node.left #if so moves onto the left node
            elif target > node.data: #checks if the target node is greater than the node
                node = node.right #moves onto the right node
            
        if node is None or node.data != target: #checks if the node is none or if anything in the node is not equivalent to the target
            return False #will return false if such
        
        elif node.left is None and node.right is None: #checks if the left node and right node are none
            if target < parent.data: #if so will check if the target is less than the parent
                parent.left = None #will make the node left to the parent none
            else:
                parent.right = None #will make node right to the parent none
            return True #will return true otherwise

        elif node.left and node.right is None: #checks if the left node is something and the right node is nothing
            if target < parent.data: #if so will check if the target is less than the parent
                parent.left = node.left #if so will make the parent's left equivalent to the main node's left
            else:
                parent.right = node.left #will make the parent's right node equivalent to the main node's left
            return True #will return true otherwise

        elif node.left and node.right is None: #checks if the left node is nothing and the right node is something
            if target > parent.data: #if so will check if the target is less than the parent
                parent.right = node.right #if so will make the parent's right equivalent to the main node's right
            else:
                parent.left = node.right #will make the parent's left node equivalent to the main node's right
            return True # will return true otherwise

        else:
            self.if_left_and_right(node) #else calls the if_left_and_right function


        




#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
print(bst.Bin_Tree_find_iterative(2))
print(bst.Bin_Tree_find_recursive(7))
bst.display(bst.root)
print(bst.remove(4))
#bst.insert(8)
#bst.insert(9)
#bst.insert(10)
#bst.insert(11)
##bst.insert(12)
##bst.insert(13)
##bst.insert(14)
##bst.insert(15)
##bst.insert(100)
##bst.insert(200)

bst.display(bst.root)
