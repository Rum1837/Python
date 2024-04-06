import turtle
turtle.shape("turtle")
turtle.speed(5)
size = int(input("введите длину стороны-"))
color = "green"

turtle.penup()
turtle.forward(size/2)
turtle.pendown()
turtle.left(90)
turtle.forward(size/2)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size/2)