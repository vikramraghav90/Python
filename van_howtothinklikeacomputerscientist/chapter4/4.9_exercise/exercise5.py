import turtle

window = turtle.Screen()
window.bgcolor("pink")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(1)


def draw_spiral(numbers, radian):
    size = 2
    for _ in range(numbers):
        tess.left(radian)
        tess.forward(size)
        size += 2


draw_spiral(50, -90)

draw_spiral(51, -88)

window.mainloop()
