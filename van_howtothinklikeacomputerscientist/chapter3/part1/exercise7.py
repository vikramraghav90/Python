# Write a program which, given the length of two sides of a right-angled triangle, returns the length of the
# hy-potenuse. (Hint:x**0.5will return the square root.)

side1, side2 = input("enter the length of two sides \n").split(' ')
hy_potenuse = (int(side1)**2 + int(side2)**2)**0.5

print(hy_potenuse)