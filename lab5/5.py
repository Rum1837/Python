import turtle
turtle.shape("turtle")
turtle.speed(5)
for i in range(1, 10000000000):
    angle = int(input("введите количество углов-"))
    size = int(input("введите длину стороны-"))
    color = input("введите цвет-")
    turtle.color(color)
    if angle < 3:
     print("углов не может быть меньше трёх")
    elif angle == 3:
     turtle.forward(size)
     turtle.left(120)
     turtle.forward(size)
     turtle.left(120)
     turtle.forward(size)
    elif angle == 4:
     turtle.forward(size)
     turtle.left(90)
     turtle.forward(size)
     turtle.left(90)
     turtle.forward(size)
     turtle.left(90)
     turtle.forward(size)