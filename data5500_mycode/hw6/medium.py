'''
Medium: (5 points)

2. Given an array of integers, write a function that finds the second largest number in the array.

Analyze the time complexity of your solution using Big O notation, 
especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''
lst2 = [1,-4,3,15,5,6,16,6,9,25]

def sec_larg(arr):
    max_lst = []
    max_num = 0 

    for i in arr:
        if i > max_num:
            max_num = i
            max_lst.append(max_num)
    return(max_lst[-2])

print(sec_larg(lst2))

# O(n): order n notation: just looping through for loop once




## -- but there is another list that it goes through, does that make it a different notation?? 
