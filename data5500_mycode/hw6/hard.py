
'''
Hard: (7 points)

3. Write a function that takes an array of integers as input and returns the maximum difference 
between any two numbers in the array.

Analyze the time complexity of your solution using Big O notation, 
especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''
lst3 = [4,7,12,9,23,5,2]
max_lst = 0
min_lst = 0
diff = 0

def max_diff():
    min_lst = min(lst3)
    max_lst = max(lst3)
    diff = max_lst - min_lst
    return diff

print(max_diff())

# O(n): order n notation: min and max are both python functions that loop through the list to find the minimum and maximum numbers,
# since it isn't a nested loop, it's still order n notation. 