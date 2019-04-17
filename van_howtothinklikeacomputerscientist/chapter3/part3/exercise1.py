# write a program to count how many odd number are in list
list = input("enter value of list\n").split(' ')
count = 0
for item in list:
    if int(item) % 2 != 0:
        count += 1
    else:
        pass

print(count)
