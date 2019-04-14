numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]
for numb in numbers:
    if numb >= 75:
        print("your marks are ", numb," and your grade is FIRST")
    elif numb < 75 and numb >= 70:
        print("your marks are ", numb," and your grade is Upper Second")
    elif numb < 70 and numb >= 60:
        print("your marks are ", numb," and your grade is Second")
    elif numb < 60 and numb >= 50:
        print("your marks are ", numb," and your grade is Third")
    elif numb < 50 and numb >= 45:
        print("your marks are ", numb," and your grade is F1 Supp")
    elif numb < 45 and numb >= 40:
        print("your marks are ", numb," and your grade is F2")
    elif numb < 40:
        print("your marks are ", numb," and your grade is F3")
    else:
        print("Number is not correct")
