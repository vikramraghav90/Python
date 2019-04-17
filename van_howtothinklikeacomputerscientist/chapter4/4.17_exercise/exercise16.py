def is_factor(f,n):
    if n % f == 0:
        return True
    else:
        return False

print(is_factor(3,12))
print(not is_factor(5, 12))