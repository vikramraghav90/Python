import turtle

window = turtle.Screen()
window.bgcolor("pink")

dore = turtle.Turtle()
dore.color("red")
dore.pensize(3)


def draw_a_square(size):
    for _ in range(4):
        dore.forward(size)
        dore.left(90)


def draw_squares(numbers):
    size = 20
    move = -10
    for _ in range(numbers):
        draw_a_square(size)
        size += 20
        dore.penup()
        dore.goto(move, move)
        dore.pendown()
        move -= 10


draw_squares(7)

window.mainloop()
