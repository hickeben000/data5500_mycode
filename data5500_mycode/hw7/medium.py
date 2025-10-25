'''
Medium: (5 points)

2. Implement a Python function to search for a value in a binary search tree. 
The method should take the root of the tree and the value to be searched as parameters. 
It should return True if the value is found in the tree, and False otherwise.
'''
# copied and pasted code from easy.py to build a tree 
class Node:
    # constructor to create a new node
    def __init__(self, key):
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

def specificValue(node, value):
    if node is None:        # if it's an empty tree, the value isn't in it
        return False
    if node.key == value:
        return True
    elif value < node.key:
        return specificValue(node.left, value)
    else: 
        return specificValue(node.right, value)

def main():
    root = None
    root = insert(root, 4)  # root refers to that Node object that stores 4.
    root = insert(root, 7)
    root = insert(root, 0)
    root = insert(root, -2)
    root = insert(root, 89)
    root = insert(root, 54)

    print(specificValue(root, -2))
    

main()



'''
Chat prompts: 
So here is my code. I am searching for my specific value (which is 7) in my tree 
and returning true if it and false if it isn't. Should i pass in two arguments 
to my specificValue function like i did with the insert function?
''' 
# why you need node.key and not just node
'''
I am not fully understanding why you need the node.key instead of just node... 
it might be a good idea to give me a quick refresher on classes

print(node)
you get something like:
<__main__.Node object at 0x000001E2C8EBA3A0>
That’s just saying: “there’s a Node object sitting in memory here.”

But if you write:
print(node.key)
you get:
7
That’s because you’re now accessing the data stored inside the Node object — 
the value of its key attribute.

if node.key == 7:
That means:
“Is the value inside this node equal to 7?”
node is an object and 7 an integer -- you can't compare them
'''
# further understanding of root. 
'''
so when i first call root in my specificValue function is that value 54, 
because that's the last value i inputed when i called my insert function?
'''
'''
here is my question and code. The code is running but i am getting a 'None' response, why is this happening?
explain step two to me more. 
'''