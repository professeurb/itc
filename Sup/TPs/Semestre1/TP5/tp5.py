## Triangle de Sierpinski

import turtle


def sierp_triangleblanc(x, y, r):
    turtle.fillcolor(255, 255, 255)
    turtle.setposition(x, y)
    turtle.setheading(60)
    turtle.begin_fill()
    turtle.forward(r)
    turtle.left(120)
    turtle.forward(r)
    turtle.left(120)
    turtle.forward(r)
    turtle.end_fill()


# Fonction à modifier
def sierp(x, y, r, n):
    if n > 0:
        sierp_triangleblanc(x, y, r)
        sierp(x, y + 3 ** 0.5 * r / 2, r / 2, n - 1)


def sierpinski(r, n):
    # réglage initial
    turtle.showturtle()
    turtle.colormode(255)
    turtle.clear()
    # tracé du triangle noir
    ## mise en place initiale
    turtle.fillcolor(0, 0, 0)
    turtle.up()
    turtle.setposition(0, 0)
    turtle.setheading(0)
    ## tracé
    turtle.down()
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(r)
        turtle.left(120)
        turtle.forward(r)
    turtle.end_fill()
    # tracé récursif des triangles intérieurs en blanc
    turtle.penup()
    turtle.fillcolor(255, 255, 255)
    sierp(0, 0, r, n)
    # on a fini
    turtle.hideturtle()


## Euclide et Bézout


def euclide(a, b):
    ...


def bezout(a, b):
    ...


## Courbe de Koch


def koch(n, l):
    ...