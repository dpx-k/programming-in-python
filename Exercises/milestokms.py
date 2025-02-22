first_name = input("Enter your name: ")
kilometers = float(input("Enter the distance in kilometers: "))

miles = round((kilometers / 1.609), 2)
print(f"Hello {first_name.capitalize()}, the distance is {miles} miles")