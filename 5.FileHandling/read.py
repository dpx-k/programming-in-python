with open("test.txt", mode = 'r') as samplefile: 
    print(samplefile.read(45))  # you can pass a number in the read function to read specific number of characters from the text 
    
    print(samplefile.readline()) # reads only the first line in the file 
    
    # in the above instance, read(45) reads the specified chars and the readline() function captures the remaining characters
    # in the first line 
    
# alterantively you can open another instance of the same file and test out the readline function 

with open("test.txt", mode = 'r') as file: 
    # print(file.readline())
    for x in file: 
        print(x)  # you can use a for loop to capture line by line, use end = "" to prevent line spacing 
    
# alternatively you can store the lines in a list and get all the functions of list, use the readlines() function
with open('test.txt', mode = 'r') as textfile:
    lines = textfile.read().splitlines()    
    print(lines)