input_string = input("Enter a list element separated by space ")
my_list  = input_string.split()
print(my_list)
count = 0
for odd in my_list:
    if len(odd) == 5:
        count = count + 1
    else:
        pass
print("strings having length 5 are ",count)
