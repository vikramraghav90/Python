import turtle

window = turtle.Screen()
window.bgcolor("pink")
dore = turtle.Turtle()
dore.color("blue")
dore.pensize(3)
dore.shape("turtle")


def draw_poly(t, lengths):
    for side in range(3):
        t.forward(lengths)
        t.right(120)


def draw_equitriangle(t, sz):
    draw_poly(t, sz)


draw_equitriangle(dore, 50)
window.mainloop()