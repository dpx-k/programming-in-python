with open('newfile.txt', 'w') as file: 
    file.write("Hello there!")
    file.writelines(["This line one", "This is line two", "This is line three"])
    
with open('newfile.txt', 'a') as edit:
    edit.write("\nappend mode adds a line at the end of the file instead of overwriting it \n")
    edit.write('The cursor starts at the end of the text file')