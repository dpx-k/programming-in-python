sentence = "Hello, World! This is Python Programming language"

# Accessing specific characters using the index 
print(sentence[0])

# Access characters from backwards using negative indexing 
print(sentence[-1]) 

# Slicing - grab a specified part of a string using indexes 
print(sentence[0:13])

# slice using negative indices
print(sentence[-20:-1])

# you can leave start or endpoints as blank
# startpoint blank - starts from 0 
# endpoint blank - grabs everything till end
print(sentence[-27:])
print(sentence[:28])