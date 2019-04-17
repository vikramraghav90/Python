import turtle

window = turtle.Screen()
window.bgcolor("pink")
zoe = turtle.Turtle()
zoe.color("blue")


def draw_a_start():
    for _ in range(5):
        zoe.forward(100)
        zoe.right(144)


draw_a_start()
window.mainloop()
