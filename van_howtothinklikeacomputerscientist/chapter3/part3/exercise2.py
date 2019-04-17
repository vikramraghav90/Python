# sum up all the even numbers in a list
list = input("enter value of list\n").split(' ')
sum = 0
for item in list:
    if int(item) % 2 == 0:
        sum += int(item)
    else:
        pass

print(sum)