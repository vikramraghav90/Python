import turtle

window = turtle.Screen()
window.bgcolor("pink")
zoe = turtle.Turtle()
zoe.color("blue")


def draw_a_start():
    for _ in range(5):
        zoe.forward(100)
        zoe.right(144)


def draw_starts():
    for _ in range(5):
        draw_a_start()
        # zoe.penup()
        zoe.forward(350)
        zoe.right(144)
        # zoe.pendown()


# What would it look like if you didn’t pick up the pen?
# def draw_starts():
#     for _ in range(5):
#         draw_a_start()
#         zoe.forward(350)
#         zoe.right(144)

draw_starts()
window.mainloop()
