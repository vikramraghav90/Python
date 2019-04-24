def reverse(string):
    my_string = ""
    for i in range(1, len(string)+1):
        my_string += string[-i]

    print(my_string)


string = input("Enter your string\n")
print(reverse(string))