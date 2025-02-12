import turtle

wn = turtle.Screen()
miranda = turtle.Turtle()

distance = 10
angle = 90 

miranda.speed(0) # varies from 0 - 10 

#speed increases as the value increases, 0 will instantly print 

for _ in range(150): 
    miranda.left(angle)
    miranda.forward(distance)
    distance += 10 

wn.exitonclick()
