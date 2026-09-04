# import turtle
# import random

# screen = turtle.Screen()
# screen.setup(width=800, height=600)

# turtle1 = turtle.Turtle()
# turtle2 = turtle.Turtle()
# turtle3 = turtle.Turtle()

# turtle1.color("red")
# turtle2.color("blue")
# turtle3.color("green")

# turtle1.shape("turtle")
# turtle2.shape("turtle")
# turtle3.shape("turtle")

# turtle1.penup()
# turtle2.penup()
# turtle3.penup()

# turtle1.goto(-300, 100)
# turtle2.goto(-300, -0)
# turtle3.goto(-300, -100)

# while True:
#     turtle1.forward(random.randint(1, 10))
#     turtle2.forward(random.randint(1, 10))
#     turtle3.forward(random.randint(1, 10))

#     if turtle1.xcor() >= 300:
#         print("Red turtle wins!")
#         break

#     if turtle2.xcor() >= 300:
#         print("Blue turtle wins!")
#         break

#     if turtle3.xcor() >= 300:
#         print("Green turtle wins!")
#         break

# screen.mainloop()


import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)

colors = ["red", "blue", "green"]
turtles = []

for i, color in enumerate(colors):
    t = turtle.Turtle("turtle")
    t.color(color)
    t.penup()
    t.goto(-300, 100 - i * 100)
    turtles.append(t)

while True:
    for t in turtles:
        t.forward(random.randint(1, 10))

        if t.xcor() >= 300:
            print(f"{t.color()[0].capitalize()} turtle wins!")
            break
    else:
        continue
    break

screen.mainloop()
