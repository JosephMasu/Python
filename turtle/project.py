import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=600)

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

turtle1.color("red")
turtle2.color("blue")
turtle3.color("green")

turtle1.shape("turtle")
turtle2.shape("turtle")
turtle3.shape("turtle")

turtle1.penup()
turtle2.penup()
turtle3.penup()

turtle1.goto(-300, 100)
turtle2.goto(-300, -0)
turtle3.goto(-300, -100)

while True:
    turtle1.forward(random.randint(1, 10))
    turtle2.forward(random.randint(1, 10))
    turtle3.forward(random.randint(1, 10))

    if turtle1.xcor() >= 300:
        print("Red turtle wins!")
        break

    if turtle2.xcor() >= 300:
        print("Blue turtle wins!")
        break

    if turtle3.xcor() >= 300:
        print("Green turtle wins!")
        break

screen.mainloop()