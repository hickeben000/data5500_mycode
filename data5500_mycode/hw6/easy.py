'''
Easy: (3 points)

1. Given an array of integers, write a function to calculate the sum of all elements in the array.

Analyze the time complexity of your solution using Big O notation, 
especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''
lst = [1,2,3,4,5,6,7,8,9,25]

print(sum(lst))

# 0(n): order n notation: the built in python function of sum is going through each element in lst and adding them up. 
