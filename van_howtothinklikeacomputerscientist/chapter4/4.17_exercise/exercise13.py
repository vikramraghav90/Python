
def slope(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    if y == 0:
        return 0
    else:
        slo = y/x
        return slo


print(slope(5, 3, 4, 2))
print(slope(1, 2, 3, 2))
print(slope(1, 2, 3, 3))
print(slope(2, 4, 1, 2))


def intercept(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    inter = y1 - (y/x) * x1
    return inter

print(intercept(1, 6, 3, 12))
print(intercept(6, 1, 1, 6))
print(intercept(4, 6, 12, 8))