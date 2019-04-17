def to_secs(hours, minutes, seconds):
    totals = hours * 3600 + minutes * 60 + seconds
    return int(totals)


print(to_secs(2, 30, 10))
print(to_secs(2, 0, 0))
print(to_secs(0, 2, 0))
print(to_secs(0, 0, 42))
print(to_secs(0, -10, 10))

#8 extend

print(to_secs(2.5, 0, 10.71))
print(to_secs(2.433, 0, 0))