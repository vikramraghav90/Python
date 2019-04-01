# 1. Write a function that returns the maximum of two numbers.

def maximum(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a and b


print(maximum(12, 10))
print(maximum(8, 99))
print(maximum(15, 15))
