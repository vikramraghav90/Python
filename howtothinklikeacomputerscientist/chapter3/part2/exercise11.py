import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
clock = turtle.Turtle()
clock.shape("turtle")
clock.color("blue")
clock.stamp()
def clock_stamp():
    move = 30
    sides = 12
    for i in range(sides):
        clock.penup()
        clock.forward(40)
        clock.pendown()
        clock.forward(20)
        clock.penup()
        clock.forward(20)
        clock.stamp()
        clock.home()
        clock.right(move)
        move = move + 30
clock_stamp()
window.mainloop()

