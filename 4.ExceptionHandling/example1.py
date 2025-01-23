items = [1,2,3,4,5]

# trying to access an element with an index with does not exist in the list
try: 
    item = items[6]
    print(item)
except Exception as e:
    print("Error:", e)
