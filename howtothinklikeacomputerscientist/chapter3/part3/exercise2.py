try: 
    my_list = [] 
      
    while True: 
        my_list.append(int(input())) 
          
# if input is not-integer, just print the list 
except: 
    print(my_list)
total = 0
for odd in my_list:
    if (odd % 2) == 0:
        total = total + odd
    else:
        pass
print("sum of even numbers is ",total)
