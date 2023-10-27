import turtle
t=turtle.Turtle()

""" c=t.clone()
t.color("blue")
c.color("green")
t.circle(30)

for i in range(4):
    for i in range(50,100,5):
     c.speed(8)
     c.circle(i)
    t.left(70)
    t.circle(30)
    c.speed(8)
    c.color("red")
    c.left(70)

turtle.mainloop() """

turtle.bgcolor("black")
t.pencolor("red")


a=0
b=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while(True):
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==210:
        break
    t.hideturtle()
turtle.mainloop()

