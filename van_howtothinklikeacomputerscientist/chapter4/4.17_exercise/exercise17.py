def is_muitiple(f,n):
    if n % f == 0 or f % n == 0:
        return True
    else:
        return False

print(is_muitiple(12, 3))
print(is_muitiple(4, 12))