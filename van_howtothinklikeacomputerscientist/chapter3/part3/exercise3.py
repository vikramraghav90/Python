# sum up all the negative numbers in a list
list = input("enter value of list\n").split(' ')
sum = 0
for item in list:
    if float(item) < 0:
        sum += float(item)
    else:
        pass

print(sum)