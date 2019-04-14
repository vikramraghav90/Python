print ("We will ask you each length of triagnle, please input longest side at last\n\n")
first_side = float(input("Please type the length of first side of a Right Andgled Triangle"))
second_side = float(input("Please type the length of second side of a Right Andgled Triangle"))
third_side = float(input("Please type the length of Third side of a Right Andgled Triangle"))
if first_side < second_side and first_side > third_side:
    longest_side = second_side
elif first_side < third_side and first_side > second_side:
    longest_side = third_side
else:
    longest_side = second_side

#def third_side(side1,side2):
#    third_side = float((first_side ** 2 + second_side ** 2) ** 0.5)
#    print("Third side of triangle is ",third_side)
#third_side(first_side,second_side)
#threshold = 1e
#if abs(x-y) < threshold:
#print(threshold)
