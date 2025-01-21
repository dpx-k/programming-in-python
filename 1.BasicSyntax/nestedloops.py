# prints a 2d array grid of 0s using nested loops 

import time 

start_time = time.time()

for i in range(100000):
    for j in range(30):
        print(0, end = " ")
    print()
    
end_time = round((time.time() - start_time), 4)

print(end_time)

# note that time taken for the execution of the program is significant for only large datasets
# try changing the range values to large numbers to notice the difference 