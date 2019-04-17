import turtle

window = turtle.Screen()
window.bgcolor("pink")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)


def draw_a_square(size):
    for _ in range(4):
        tess.forward(size)
        tess.left(90)


def draw_squares(size):
    for _ in range(20):
        draw_a_square(size)
        tess.left(18)


draw_squares(100)

window.mainloop()
