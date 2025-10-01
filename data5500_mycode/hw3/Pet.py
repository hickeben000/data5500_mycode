'''
Hard Question (7 points)

3.    Create a class called Pet with attributes name and age. 
Implement a method within the class to calculate the age of the 
pet in equivalent human years. Additionally, create a class 
variable called species to store the species of the pet. 
Implement a method within the class that takes the species of 
the pet as input and returns the average lifespan for that species.

- Instantiate three objects of the Pet class with different names, 
ages, and species.
- Calculate and print the age of each pet in human years.
- Use the average lifespan function to retrieve and print the average 
lifespan for each pet's species.
'''
import numpy as np


class pet():
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species.lower()

    def toHumanYears (self):
        if self.species == "dog":
            if self.age == 1:
                return 15
            if self.age ==2:
                return 24 
            else:
                return 24 + (self.age - 2) * 5
        # how to calculate dog years specific to human years?
        # i am a bit confused by this question, do you think they want the average lifespan of the dog in dog or human years. 
        # If it is in human years how to i store the new variable i calculate in the previous function inorder to use it in my next function?
        if self.species == "cat":
            if self.age == 1:
                return 15
            if self.age == 2:
                return 24
            else:
                return 24 + (self.age - 2) * 4
        # calculate a cat's age to human years

        if self.species == "frog":
            return (self.age / 10) * 80 
        # convert a frog age to human years

    # explain to me  the average_lifespan function
    def averageLifespan (self, species):
        if self.species == "dog":
            return 13
        if self.species == "cat":
            return 15
        if self.species == "frog": 
            return 10 
    # show me what it would look like if i didn't put the lifespans in a dictionary

pet1 = pet("messi", 9, "dog")
pet2 = pet("mazi", 7, "cat")
pet3 = pet("parry", 3, "frog")

print("Messi is",pet1.toHumanYears(),"in human years.")
print("Mazi is",pet2.toHumanYears(),"in human years.")
print("Parry is",pet3.toHumanYears(),"in human years.")

print("average lifespan of a dog is", pet1.averageLifespan("dog"),"dog years.")
print("average lifespan of a cat is", pet2.averageLifespan("cat"),"cat years.")
print("average lifespan of a frog is", pet3.averageLifespan("frog"),"frog years.")

        