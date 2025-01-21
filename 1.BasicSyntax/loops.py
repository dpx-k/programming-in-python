desserts = [
    "Chocolate lava cake",
    "Tiramisu",
    "Apple pie à la mode",
    "Crème brûlée",
    "New York cheesecake",
    "Molten chocolate chip cookies",
    "Vanilla bean ice cream",
    "Strawberry shortcake",
    "Bread pudding with caramel sauce",
    "Triple chocolate mousse"
]

print('Printing Elements using for loop: ')
# iterating through each element of the list using for loop 
for dessert in desserts: 
    print(dessert)

print("\nEnumeration using for loop")
# enumerating each element using the enumerate() function 
for index, dessert in enumerate(desserts):
    print(index+1, dessert)

print("\nPrinting the elements using while loop: ")  
# iterating through each element using a while loop 
count = 0
while count < len(desserts):
    print(count+1, desserts[count])
    count += 1
    
# The pass statement allows you to run through the loop in its entirety 
# and effectively ignore that the if condition has been satisfied.

for dessert in desserts:
    if dessert == 'New York chessecake':
        pass
    print('Other desserts I like are', dessert) 

    