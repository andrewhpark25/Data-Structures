"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
         # compare the value to the root's value to determine which direction 
         # we're gonna go in
         # if the value < root's value
            if value < self.value:
             # go left
             # how do we go left
             # we have to check if there is another node on the left side
                if self.left:
                    # then self.left is a Node
                    # now what?
                    self.left.insert(value)
                else:
                    #then we can park the value here
                    self.left = BSTNode(value)
        # else the value >= root's value
            else:
            # go right
            # how do we go right?
            # we have to check if there is another node on the right side
                if self.right:
                    # then self.right is a Node
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when search start, self becomes root
        # compare target against self
        # return false when there's nothing in left or right direction
        if target == self.value:
            return True
        if target < self.value:
        # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
        # go right if right is a BSTNode
            if not self.right:
                return False
            return  self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until there's no more node on the right
        if not self.right:
            return self.value
        # otherwise, keep going right
        return self.right.get_max()
    
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the fn on value at this node
        fn(self.value)

        # pass this function to the left child
        if self.left:
            self.left.for_each(fn)
            # pass this function to the right child
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    
    
    def bft_print(self, node):
        queue = deque()
        # add the root node
        queue.append(self)
        # loop so long as the queue still has elements
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        # add the root node
        stack.append(self)
        # loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)
                            
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
   # def pre_order_dft(self, node):
    #    pass

    # Print Post-order recursive DFT
    #def post_order_dft(self, node):
     #   pass
