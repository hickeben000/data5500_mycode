'''
Easy Question: (3 points)

1.    Create a class called Rectangle with attributes length and width. 
Implement a method within the class to calculate the area of the rectangle. 
Instantiate an object of the Rectangle class with length = 5 and width = 3, and print its area.
'''
# give me the syntex i need to create a class in python
# when i initiate the class and then call that class in my 'my_car = ...' code does it go through the code after 'class Car:..' like calling a function would or am I not understanding this right?

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width 

# when do i need to include 'self' in my class and when do i not need to
    def area(self):
        area = self.length * self.width 
        return area 
# class Rectangle(): def _int__(self, length, width): self.length = length self.width = width def area(self): area = length * width return area rec = Rectangle(5, 3) print(rec.area()) why is my error saying Rectangle() need no arguments. How to i create an object that uses the blueprint i created when i initilized my class?
# So with my previous code why wasn't it seeing the width and length in my area function. Explain it to me in laman terms
rec1 = Rectangle(5, 3)
# so in this example does rec1 and rec2 become self? when you send in the parameters 5,3 and 10,20. like is a good way to think of this would be like sending functions into a parameter, where rec1 takes the self spot in the class, 5 will take the length and 3 the width?p

print(rec1.area())

# how do i run my code from the terminal in an ec2 environment?
