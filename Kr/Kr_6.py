import turtle

t = turtle
t.shape("turtle")
t.pensize(3)
turtle.speed(2000)

kol_vo = 4
radius = int(input("Ввод радиуса: "))
colors = ["blue","orange","green","red"]

for i in range(kol_vo+1):
    color = colors[i%4]
    t.circle(radius*i)
    t.up()
    t.sety((radius*i)*(-1))
    t.down()
    t.pencolor(color)
input("Продожить на кнопку")