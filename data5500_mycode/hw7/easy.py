'''
Easy: (3 points)

Write a Python function to insert a value into a binary search tree. 
The function should take the root of the tree and the value to be inserted as parameters.
'''
class Node:
    # constructor to create a new node
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None 

def insert(node, key):
    if node is None: 
        return Node(key) # calls on the class to create a new node (an object) 
    
    if key < node.key:  # determine if number you're inputting is less than the root / what ever circle we are currently on
        node.left = insert(node.left, key) # changes the node to the current circle and recalls function to see if it's the lowest number 
    else: 
        node.right = insert(node.right, key) 

    return node 

def main():
    root = None
    root = insert(root, 4)


'''
ChatGPT entry: copy and pasted my code and the question to see if Chatgpt agreed that I answered the question fully.

Easy: (3 points) Write a Python function to insert a value into a binary search tree. 
The function should take the root of the tree and the value to be inserted as parameters. 
class Node: # constructor to create a new node def __init__(self,key): self.key = key self.left = None self.right = None 
def insert(node, key): if node is None: return Node(key) # calls on the class to create a new node (an object) if key < node.key:
     # determine if number you're inputting is less than the root / what ever circle we are currently on node.left = insert(node.
     left, key) # changes the node to the current circle and recalls function to see if it's the lowest number else: node.right =
      insert(node.right, key) return node def main(): root = None root = insert(root, 4)
 here is my question and the code i typed out. Do you think this code accurately answers this question?
 '''