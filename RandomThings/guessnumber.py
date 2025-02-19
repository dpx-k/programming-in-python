import random 

def take_input(): 
    num = int(input("Guess the Number: "))
    return num

key = random.randint(1, 100)
chances = 5

# print("Generated number: ", key)

guess = 0
end_game = False

while not end_game: 
    print(f"\rChances left: {chances} ", end = "", flush = True)
    guess = take_input()

    if key == guess: 
        print("You guessed it right!")
        break
    elif key < guess: 
        print("The number is less than your guess! ")
    else: 
        print("The number is greater than your guess! ")

    chances -= 1

    if chances == 0: 
        print("you ran out of chances! ")
        print("The number was: ", key)
        end_game = True
    
    