import turtle


def square(color='black'):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.color(color)
        turtle.forward(25)
        turtle.right(90)
    turtle.end_fill()


def avancer(forward=100, angle=90, direction="droite", avant=False):
    if avant:
        turtle.forward(forward)

    if direction == "droite":
        turtle.right(angle)
    else:
        turtle.left(angle)

    if not avant:
        turtle.forward(forward)


def main():
    turtle.fillcolor('white')
    turtle.begin_fill()
    for i in range(4):
        avancer(forward=200, avant=True)
    turtle.end_fill()
    turtle.up()
    avancer()
    turtle.left(90)
    turtle.down()
    square()
    turtle.up()
    turtle.forward(175)
    turtle.down()
    square()
    turtle.up()
    avancer(forward=50)
    avancer(forward=25)
    turtle.down()
    for i in range(4):
        square()
        turtle.forward(25)
    avancer(forward=50, angle=180)
    turtle.right(90)
    square()
    turtle.left(90)
    square('red')
    turtle.forward(25)
    square('red')
    turtle.done()


main()
