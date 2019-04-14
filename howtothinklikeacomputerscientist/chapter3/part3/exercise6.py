input_string = input("Enter a list element separated by space ")
my_list  = input_string.split()
print(my_list)
count = 0
for odd in my_list:
    if odd == "sam":
        break
    else:
        count = count + 1
if count == len(my_list):
    print("no string \"sam\" is present, and the total number of elements are", count)
else:
    print("Number of words till string \"sam\" are ",count)
