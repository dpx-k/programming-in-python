# Variable Length Arguments - Any number of arguments can be passed into the function

def add(*args):
    sum = 0; 
    for x in args: 
        sum += x
    
    return sum

print(add(1,2,46,342,2452))