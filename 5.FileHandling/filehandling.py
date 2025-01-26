file = open("test.txt", mode = 'r')

data = file.readline() # reads a single line from the text 
full_text = file.read()

print(data, '\n')
print(full_text)

file.close()