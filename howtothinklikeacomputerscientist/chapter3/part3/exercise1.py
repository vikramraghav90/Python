try: 
    my_list = [] 
      
    while True: 
        my_list.append(int(input())) 
          
# if input is not-integer, just print the list 
except: 
    print(my_list)
count = 0
for odd in my_list:
    if (odd % 2) != 0:
        count = count + 1
    else:
        pass
print("odd numbers are ",count)
