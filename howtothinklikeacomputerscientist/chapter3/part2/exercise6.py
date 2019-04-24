import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
#tess.shape("turtle")
tess.color("blue")
tess.setheading(0)
for i in (160, -43, 270, -97, -43, 200, -940, 17, -86):
        tess.left(i)
        tess.forward(100)
window.mainloop()

