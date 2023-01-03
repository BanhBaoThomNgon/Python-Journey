import turtle
testudo = turtle.Turtle()

def polygon(sides, length):
    angles = 360 / sides
    print(angles)
    turtle.speed(1)
    for i in range(sides):
        turtle.forward(length)
        turtle.right(angles)

    for j in range(sides):
        turtle.right(angles)
        turtle.forward(length)
polygon(6, 50)