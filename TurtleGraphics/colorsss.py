import turtle

# color_input = input("Choose a color: ")

window = turtle.Screen()
window.bgcolor("cyan")

helene = turtle.Turtle()
helene.color('orange')
helene.pensize(3)

helene.forward(120)
helene.left(75)
helene.forward(200)

window.exitonclick()