import turtle

window = turtle.Screen()
window.bgcolor("pink")
window.title("Draw a square")

dore = turtle.Turtle()
dore.color("red")
dore.pensize(3)
dore.penup()
dore.setposition(-200, 0)

def draw_a_square():
    for _ in range(4):
        dore.pendown()
        dore.forward(20)
        dore.left(90)
        dore.penup()
    dore.forward(60)


def draw_squares(numbers):
    for _ in range(numbers):
        draw_a_square()


draw_squares(7)

window.mainloop()
