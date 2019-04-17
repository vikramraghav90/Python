import turtle

window = turtle.Screen()
window.bgcolor("pink")
tess = turtle.Turtle()
tess.color("red")
tess.pensize(3)


def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        t.left(360 / n)


draw_poly(tess, 8, 50)
window.mainloop()
