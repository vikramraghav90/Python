first_side = float(input("Please type the length of first side of a Right Andgled Triangle"))
second_side = float(input("Please type the length of second side of a Right Andgled Triangle"))
def third_side(side1,side2):
    third_side = float((first_side ** 2 + second_side ** 2) ** 0.5)
    print("Third side of triangle is ",third_side)
third_side(first_side,second_side)
