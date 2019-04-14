try: 
    my_list = [] 
      
    while True: 
        my_list.append(int(input())) 
          
# if input is not-integer, just print the list 
except: 
    print(my_list)
total = 0
count = 0
for odd in my_list:
    if (odd % 2) == 0:
        break
    else:
        total = total + odd
        count = count +1
if count == len(my_list):
    print("no even number is present, but the sum of all elements is ", total)
else:
    print("sum of odd numbers till we encounter first even number is ",total)

