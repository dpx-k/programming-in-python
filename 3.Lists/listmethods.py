num_list = [10,20,30,40,50,60,70,80,90,100]
sample = [911, 100, 101, 108, 234]

'''Adding elements to a list'''

#append(item) - adds a single item to the end of the list
num_list.append(110)
num_list.append(69)

#extend(iterabel) - adds elements of an iterable(ex: tuple or anotherl list) to the end of the list, can also concatenate lists into one long list 
num_list.extend([1,2,3])
print(num_list)
num_list.extend(sample)
print(num_list)
#insert(index, item) - inserts an element at the specified index
num_list.insert(9, 96)
print(num_list)

# you can replace an element by specifying the index and using the assignment operator '='. note that it replaces, does not add 
num_list[3] = 28

'''Deleting Elements from a list'''

#remove(item) - removes the first occurence of a specified element
num_list.remove(69)

#pop(index) - removes and returns the item at the specified index.
# if no index is given, it removes the last item 
num_list.pop()
num_list.pop(4)

# clear() - removes all elements from the list
mylist = [1,2,3,4,65,6,67,7,7,76,5,4,44,4,43,3,2,21]
mylist.clear()

print(num_list)

# the 'del' keyword can be used to delete an element from list 
test_list = [6,7,8,3,4,9,1,4,2]
del test_list[3]
print(test_list)

'''Searching and Counting'''

# index(item, start, end): returns the index of the first occurence of the item. 
# optional start and end parameter to define the range of search 

biglist = [347, 892, 156, 723, 445, 901, 238, 564, 789, 123, 
            678, 234, 567, 890, 432, 765, 753,  321, 654, 987, 543, 
            210, 876, 345, 789, 456, 234, 567, 890, 123, 478, 
            935, 612, 847, 159, 753, 753]

print(biglist.index(892))
print(biglist.index(345, 20, 35))

# count(item) - returns the number of occurences of the item 

print(biglist.count(753))


'''Sorting and Reversing'''

# sort(key = None, reverse = false) - Sorts the list in ascendeing order
# set reverse = True for descending order 
# the key parameter can be used to customize sorting 
# modifies the original list

sample_list = [10,3,23,65,76,34,12,34,90,1]
sample_list.sort()
print(sample_list)

sample_list.sort(reverse = True)
print(sample_list)

# sorted(list, key=None, reverse = False) - returns a new sorted list without modifying the original 
unsorted_list = [347, 892, 156, 723, 445, 901, 238, 564, 789, 123, 
                 678, 234, 567, 890, 432]
sorted_list = sorted(unsorted_list)
print(sorted_list)

# reverse() - Reverses the elements of the list in place, doesn't sort
num_list.reverse()
print(num_list)

'''Copying'''

#copy() - returns a shallow copy of the list 
lst = [1,2,3,4,5,6,7,8,9.10]
new_lst = lst.copy()

print(new_lst)