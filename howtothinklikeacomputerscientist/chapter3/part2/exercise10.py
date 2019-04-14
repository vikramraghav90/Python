import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
star = turtle.Turtle()
star.shape("turtle")
star.color("blue")
no_of_sides = int(input("How many sides of regular polygon you want to draw with my intelligent turtle"))
length = int(input("Type of length of side"))
def regular_polygon(sides,leng):
    total_angle = 360 * 2
    angle = total_angle / sides
    print("Angle we need to turn on each side is ", angle)
    for i in range(sides):
        star.forward(leng)
        star.right(angle)

regular_polygon(no_of_sides,length)
window.mainloop()

