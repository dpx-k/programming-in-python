# This python program demonstrates nested functions and global, variable and local scope in python a

def addition(a,b): 
    total = a + b
    
    def subtraction(c,d):
        difference = total + (c - d) # total variable can be accessed from the addition function demonstrating enclosed scope
        return difference
    
    difference = subtraction(a,b)
    return total, difference

def multiplication(x,y):
    global product # this variable now can be accessed anywhere in the program 
    product = x * y     
    return product 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total_sum, total_difference= addition(a,b) # stores two different values returned by the addition function
print(total_sum, total_difference)

# accessing the variable declared using the global keyword 
multiplication(a,b) 
print(product)

print(total)
# NameError: name 'total' is not defined, local variable cannot be accessed in the main program


