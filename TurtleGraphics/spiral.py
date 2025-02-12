import turtle

wn = turtle.Screen()
miranda = turtle.Turtle()

distance = 10
angle = 90 

for _ in range(40): 
    miranda.left(angle)
    miranda.forward(distance)
    distance += 10 

wn.exitonclick()
