with open('test.txt', mode = 'r') as file: 
    print(file.read())
    
# the with keyword automatically closes the file 
# it works better with exception handling 

