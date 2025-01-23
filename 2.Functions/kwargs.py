# with keyword arguments you can pass any number of keyword arguments and non keyword variables 

def multiply(**kwargs):
    
    product = 1
    for k,v in kwargs.items(): 
        product *= v
        
    return round(product, 4)


answer = multiply(num1 = 345, num2 = 325.35)
print(answer)