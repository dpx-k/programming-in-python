with open('test.txt', mode = 'r') as file: 
    print(file.read())
    
# the with keyword automatically closes the file 
# it works better with exception handling 

# general syntax is: 
# with open(file_name.txt, mode = " ") as file: 