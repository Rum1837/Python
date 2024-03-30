import turtle

# Set up turtle
turtle.shape("turtle")
turtle.speed(5)

# Draw the square
size = 100
turtle.color("green")
for _ in range(4):
    turtle.forward(size)
    turtle.left(90)

turtle.left(90)
turtle.forward(size)
turtle.right(45)
turtle.forward(size/1.4)
turtle.right(90)
turtle.forward(size/1.4)
turtle.right(45)
turtle.forward(size)
turtle.right(90)
turtle.forward(size/5)
turtle.right(90)
turtle.forward(size/2)
turtle.left(90)
turtle.forward(size/4)
turtle.left(90)
turtle.forward(size/2)

turtle.done()
