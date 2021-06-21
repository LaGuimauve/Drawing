import turtle


def square(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.color(color)
        turtle.forward(25)
        turtle.right(90)
    turtle.end_fill()


def guniv():
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.up()
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.down()
    square('black')
    turtle.up()
    turtle.forward(175)
    turtle.down()
    square('black')
    turtle.up()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.down()
    for i in range(4):
        square('black')
        turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    square('black')
    turtle.left(90)
    square('red')
    turtle.forward(25)
    square('red')
    turtle.done()

guniv()