def divide(a,b):
    return a/b; 

try: 
    print(divide(1,0))
except:
    print("Something went wrong!")  

# one way of writing the except block 
try: 
    print(divide(2,0))
except Exception as e:
    print("Something went wrong!")
    print(e.__class__)                  # gives out the class of the error
    

# Another way of doing it 

try: 
    print(divide(3,0))
except Exception as e:
    print("Error: ", e)
    print(e.__class__)                  # actual type of class of exception
    
    
     
    