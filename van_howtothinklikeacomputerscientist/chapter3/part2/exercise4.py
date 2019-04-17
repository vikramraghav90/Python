numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# (a) print each of the number on the new line
for item in numbers:
    print(item, "\n")

# (b) print each number and its square on the new line
for item in numbers:
    print(item, ":", item**2, "\n")

# (c) print total
total = 0
for item in numbers:
    total += item
print("sum of all numbers is", total, "\n")

# (d) print product
product = 1
for item in numbers:
    product *= item
print("product of all numbers is", product, "\n")
