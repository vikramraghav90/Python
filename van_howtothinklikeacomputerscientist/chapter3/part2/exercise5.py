# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the
# same):
# •  An equilateral triangle
# •  A square
# •  A hexagon (six sides)
# •  An octagon (eight side)

import turtle

window = turtle.Screen()
window.bgcolor("pink")
dore = turtle.Turtle()
dore.color("blue")
dore.pensize(3)
dore.shape("turtle")

sides = int(input("Enter sides of regular do you want : 3 , 4, 6 or 8\n"))
lengths = int(input("Enter length of side\n"))

for side in range(sides):
    dore.forward(lengths)
    dore.right(360/sides)

window.mainloop()
