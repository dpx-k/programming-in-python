# to pick a random name from the petname text file 

import random

file = open('petnames.txt', mode = 'r')

# file_content = file.read()
data = file.read()
name_list = data.split('\n')

print(name_list, '\n')

print('Choice: ', random.choice(name_list))

file.close()