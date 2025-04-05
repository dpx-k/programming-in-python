file = open("test.txt", mode = 'r') # open the file 

data = file.readline() # reads a single line from the text 
full_text = file.read() # reads the full file 

print(data, '\n')
print(full_text)

file.close() # close the file 