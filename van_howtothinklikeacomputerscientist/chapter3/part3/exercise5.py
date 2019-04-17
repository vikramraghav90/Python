# Sum all the elements in a list up to but not including the first even number (What if there is no even number?)
list = input("enter value of list\n").split(' ')
count = sum = 0

for item in list:
    if int(item) % 2 != 0:
        count += 1
        if count == 1:
            continue
        else:
            sum += int(item)
    else:
        sum += int(item)

print(sum)
