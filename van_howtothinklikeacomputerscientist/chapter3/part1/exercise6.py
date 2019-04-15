numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for mark in numbers:
    if mark >= 75:
        print("your marks are ", mark, " and your grade is FIRST")
    elif 75 > mark >= 70:
        print("your marks are ", mark, " and your grade is Upper Second")
    elif 70 > mark >= 60:
        print("your marks are ", mark, " and your grade is Second")
    elif 60 > mark >= 50:
        print("your marks are ", mark, " and your grade is Third")
    elif 50 > mark >= 45:
        print("your marks are ", mark, " and your grade is F1 Supp")
    elif 45 > mark >= 40:
        print("your marks are ", mark, " and your grade is F2")
    elif mark < 40:
        print("your marks are ", mark, " and your grade is F3")
    else:
        print("no exist")
