# trying to open a file which does not exist

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e: 
    print("Error: ", e)