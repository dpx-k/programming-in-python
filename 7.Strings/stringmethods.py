sentence = "Hello, World! This is Python Programming language"

#returns the length of the string 
print(len(sentence))

#convert all characters to lower Case
print(sentence.lower())

#convert all characters to upper case 
print(sentence.upper())

#Capitalise the first character in a string 
print(sentence.capitalize()) # converts all other characters to lowercase 

#Capitalise the first character in all the words
print(sentence.title())

#find the number of instances of a specified pattern 
print(sentence.count('P'))

#find the index of the specified character 
print(sentence.find('P'))  #if there is recurring characters, it'll return the index of the first found char
print(sentence.find('Python')) # if you try to pass a full string it again returns the index of the first char of the passed string 

# replace a part of string 
print(sentence.replace('Python', 'Java')) # as strings are immutable, the value cannnot be updated but can be stored in a new string 

updated_sentence = sentence.replace("Python", "Java")
print(updated_sentence)

#you can check if a specified string is present or not using the 'in' operator 
print('Python' in sentence) # returns a boolean 'true' value
print('Python' not in sentence) # returns false