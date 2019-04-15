length = []
length = input("Enter length of three sides of a triangle, example: 3 4 5\n").split(' ')

sort_length = sorted(length, reverse=True)
max_length = int(sort_length[0])
middle_length, minimum_length = int(sort_length[1]), int(sort_length[2])

# # 1st way
# a = middle_length**2 + minimum_length**2
# b = max_length**2
# if a == b:
#     print(True)
# else:
#     print(False)

# 2nd way
threshold = 1e-7  # 1e-7 == 1 x 10^(-7)
x = (middle_length ** 2 + minimum_length ** 2) ** 0.5
y = max_length

if abs(x - y) < threshold:
    print(True)
else:
    print(False)
