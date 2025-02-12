import turtle 

window = turtle.Screen()
june = turtle.Turtle()

distance = 1
angle = 3

june.speed(0)

# june.penup()

for _ in range(1000):
    june.forward(distance)
    june.left(angle)
    distance += 0.01