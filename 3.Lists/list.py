list1 = [10,20,30,40,50]
# lists are mutable and are indexed 

# Accessing an element by index 
print(list1[3])

# Lists can contain elements of any data type mixed together 
list2 = [10, 3,14, "Python"]

# Lists can be nested into another list 
list3 = [["This", 'is', 'list'], list1, list2]

# to print the elements of a list: 
# Method 1: use the print function 
print(list1)                            # Directly print the list 
print()

# Method 2: use the asterisk operator 
print(*list1)                           # Eliminate commas and square brackets
print()

# Method 3: use a for loop 
for num in list1:                       # Print each element in a newline, use a separator to print elements like in method 2
    print(num)
    # print(num, end = " ")
    
# the len() function can be used to get the length of any iterable, it can be used for lists too 
print(len(list1))