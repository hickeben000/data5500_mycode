'''
Medium Question  (5 points)

2.  Create a class called Employee with attributes name and salary. 
Implement a method within the class that increases the salary of 
the employee by a given percentage. Instantiate an object of the 
Employee class with name = "John" and salary = 5000, 
increase the salary by 10%, and print the updated salary.
 '''
# for this problem I wrote the code by myself and then inputted my answer to chat to see ways I could improve it. 

# ''' Medium Question (5 points) 2. Create a class called Employee with attributes name and salary. Implement a method within the class that increases the salary of the employee by a given percentage. 
# Instantiate an object of the Employee class with name = "John" and salary = 5000, increase the salary by 10%, and print the updated salary. ''' here is my code that worked: increaseSalary = .10 
# class Employee(): def __init__(self, name, salary): self.name = name self.salary = salary def salaryraise(self): updatedSalary = (increaseSalary * self.salary) + self.salary return updatedSalary 
# John = Employee("John", 5000) print(John.salaryraise()) walk me through it step by step and tell me if there's anything you would do to improve it

increaseSalary = .10

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def salaryraise(self):
        updatedSalary = (increaseSalary * self.salary) + self.salary
        return updatedSalary

John = Employee("John", 5000)

print(John.salaryraise()) 



